import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_mkv_files(folder_path, base_name):
    # Regex to detect season and episode numbers
    pattern = re.compile(r"[Ss](\d+)[Ee](\d+)")
    renamed_files = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".mkv"):
            match = pattern.search(filename)
            if match:
                season = match.group(1).zfill(2)  # Zero-pad season
                episode = match.group(2).zfill(2)  # Zero-pad episode
                new_name = f"{base_name} S{season}E{episode}.mkv"
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_name)
                
                os.rename(old_path, new_path)
                renamed_files += 1

    return renamed_files

def select_folder():
    folder = filedialog.askdirectory(title="Select Folder Containing MKV Files")
    folder_var.set(folder)

def start_renaming():
    folder_path = folder_var.get()
    base_name = base_name_var.get()

    if not folder_path:
        messagebox.showerror("Error", "Please select a folder.")
        return
    if not base_name:
        messagebox.showerror("Error", "Please enter a base name.")
        return

    try:
        renamed_count = rename_mkv_files(folder_path, base_name)
        messagebox.showinfo("Success", f"Renamed {renamed_count} files successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("MKV File Renamer")

# Folder selection
folder_var = tk.StringVar()
tk.Label(root, text="Folder:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=folder_var, width=40).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=5)

# Base name input
base_name_var = tk.StringVar()
tk.Label(root, text="Base Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Entry(root, textvariable=base_name_var, width=40).grid(row=1, column=1, padx=10, pady=5)

# Start button
tk.Button(root, text="Rename Files", command=start_renaming, width=20).grid(row=2, column=0, columnspan=3, pady=10)

# Start the GUI loop
root.mainloop(
