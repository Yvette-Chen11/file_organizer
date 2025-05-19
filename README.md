Overview

Smart File Organizer is designed for students, professionals, and anyone dealing with a large number of unorganized files. Using a clean graphical user interface (GUI), users can easily select a target folder and choose an organization mode:
- Keyword-Based: Automatically identifies the most common words in filenames and groups files accordingly.
- File Type-Based: Groups files by their file extensions (e.g., .pdf, .jpg, .docx).
No files are overwritten—if duplicates exist, they are safely renamed.

Features

- Organize files in just one click
- Two smart modes: keyword-based or file type-based
- Easy-to-use interface (built with tkinter)
- Automatically handles duplicate filenames
- Works offline and requires no setup beyond Python

How to Use

Run the Python script:
python file_organizer.py
In the GUI:
Click “Browse” to select the folder you want to organize
Choose between:
📎 File Name Keywords
🧾 File Type
Click “Organize Files”
The application will automatically create categorized subfolders and move files accordingly.

Requirements

Python 3.x
Standard libraries only (os, shutil, re, tkinter, collections)
No additional packages are needed.
