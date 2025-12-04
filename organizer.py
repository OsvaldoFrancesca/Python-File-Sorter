import os
import shutil

# --- CONFIGURATION ---
# Target directory: currently set to local for safety during testing.
# TODO: In v2, implement argparse to accept path via CLI arguments.
TARGET_DIR = '.'

# Mapping extensions to destination folders.
# Using a Dictionary is cleaner and faster (O(1)) than multiple if/elif statements.
EXTENSIONS_MAP = {
    # Images
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images', '.svg': 'Images',
    # Documents
    '.pdf': 'Documents', '.txt': 'Documents', '.docx': 'Documents', '.xlsx': 'Documents',
    # Archives & Installers
    '.zip': 'Archives', '.rar': 'Archives', '.exe': 'Installers', '.msi': 'Installers',
    # Media
    '.mp4': 'Videos', '.mp3': 'Audio', '.wav': 'Audio'
}

def organize_files():
    print(f"--- STARTING CLEANUP IN: {os.path.abspath(TARGET_DIR)} ---")

    # Get all items in the directory
    try:
        files = os.listdir(TARGET_DIR)
    except FileNotFoundError:
        print("Error: Target directory not found.")
        return

    move_count = 0

    for filename in files:
        # SAFETY CHECK: Never move the script itself while it's running.
        if filename == os.path.basename(__file__):
            continue

        file_path = os.path.join(TARGET_DIR, filename)

        # Skip directories. We only want to organize loose files to avoid breaking folder structures.
        if os.path.isdir(file_path):
            continue

        # Extract extension. 
        # .lower() is crucial: '.JPG' and '.jpg' should be treated the same.
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        if extension in EXTENSIONS_MAP:
            folder_name = EXTENSIONS_MAP[extension]
            folder_path = os.path.join(TARGET_DIR, folder_name)

            # Lazy creation: Only create the folder if we actually have files to put in it.
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # File operation wrapped in try-block to handle potential permission errors 
            # (e.g., file currently open in another program).
            try:
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"[OK] Moved: {filename} -> {folder_name}/")
                move_count += 1
            except Exception as e:
                print(f"[ERR] Failed to move {filename}: {e}")
        else:
            # Files with unknown extensions are left untouched.
            pass

    print(f"--- OPERATION COMPLETE. Files moved: {move_count} ---")

if __name__ == "__main__":
    organize_files()