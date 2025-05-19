import os
import shutil
import re
from collections import Counter
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_keywords(filename):
    name = os.path.splitext(filename)[0].lower()
    words = re.findall(r'\b[a-zA-Z0-9]{4,}\b', name)
    return words

def find_top_keywords(folder_path, top_n=5):
    word_counter = Counter()
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and not filename.startswith('.'):
            words = extract_keywords(filename)
            word_counter.update(words)
    return [word for word, _ in word_counter.most_common(top_n)]

def assign_category_by_keyword(filename, top_keywords):
    words = extract_keywords(filename)
    for word in words:
        if word in top_keywords:
            return word.upper()
    return 'Others'

def assign_category_by_filetype(filename):
    ext = os.path.splitext(filename)[1].lower()
    return ext[1:].upper() if ext else "Others"

def get_unique_path(dest_path):
    base, ext = os.path.splitext(dest_path)
    counter = 1
    while os.path.exists(dest_path):
        dest_path = f"{base}_{counter}{ext}"
        counter += 1
    return dest_path

def organize_files(folder_path, mode):
    if mode == "keyword":
        top_keywords = find_top_keywords(folder_path)
    else:
        top_keywords = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and not filename.startswith('.'):
            if mode == "keyword":
                category = assign_category_by_keyword(filename, top_keywords)
            else:
                category = assign_category_by_filetype(filename)

            target_folder = os.path.join(folder_path, category)
            os.makedirs(target_folder, exist_ok=True)
            dest_path = get_unique_path(os.path.join(target_folder, filename))
            try:
                shutil.move(file_path, dest_path)
            except Exception as e:
                print(f"Error moving {filename}: {e}")

    return top_keywords if mode == "keyword" else None

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def start_organizing():
    folder = folder_var.get()
    mode = mode_var.get()
    if not os.path.isdir(folder):
        messagebox.showerror("Error", "Invalid folder path!")
        return

    top_keywords = organize_files(folder, mode)
    if mode == "keyword":
        messagebox.showinfo("Done", f"Files organized by keywords:\n{', '.join(top_keywords)}")
    else:
        messagebox.showinfo("Done", f"Files organized by file type!")

# Set-up user interface
root = tk.Tk()
root.title("🗂️ Smart File Organizer")
root.geometry("400x300")

folder_var = tk.StringVar()
mode_var = tk.StringVar(value="keyword")  #Set the default method to 'keyword'

tk.Label(root, text="Select Folder to Organize", font=('Arial', 12)).pack(pady=10)
tk.Entry(root, textvariable=folder_var, width=40).pack()
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)

tk.Label(root, text="Organize By:", font=('Arial', 12)).pack(pady=10)
tk.Radiobutton(root, text="📎 File Name Keywords", variable=mode_var, value="keyword").pack()
tk.Radiobutton(root, text="🧾 File Type", variable=mode_var, value="filetype").pack()

tk.Button(root, text="Organize Files", command=start_organizing,
          bg='green', fg='black', width=20).pack(pady=20)

root.mainloop()