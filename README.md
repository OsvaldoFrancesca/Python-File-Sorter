# 📂 Python File Sorter

A lightweight, efficient automation script designed to organize cluttered directories by sorting files into subfolders based on their extensions.

Built with **Python 3**, focusing on safety and maintainability using standard libraries (`os`, `shutil`).

## 🚀 Features
- **Zero Dependencies:** Uses only Python Standard Library.
- **Safe Execution:** Includes self-exclusion logic to prevent the script from moving itself.
- **Error Handling:** `try/except` blocks ensure the script continues running even if a specific file is locked or in use.
- **O(1) Lookup:** Uses a dictionary hash map for extension matching instead of nested `if/else` statements.

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OsvaldoFrancesca/Python-File-Sorter.git
Navigate to the directory:

Bash

cd Python-File-Sorter
Run the script: Place the organizer.py script inside the folder you want to clean, then run:

Bash

python organizer.py
Note: The script currently targets the directory it is located in (.).

⚙️ Configuration
You can easily customize where files go by modifying the EXTENSIONS_MAP dictionary at the top of organizer.py:

Python

EXTENSIONS_MAP = {
    '.jpg': 'Images',
    '.pdf': 'Documents', 
    # Add your own: '.extension': 'Folder_Name'
}
📄 License
This project is licensed under the MIT License - feel free to use and modify it.
