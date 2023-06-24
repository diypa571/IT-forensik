/*
Diyar - LIU
diypa571@gmail.com

*/

import os
import glob

def get_removed_files():
    trash_path = os.path.expanduser("~/.local/share/Trash/files")  # Path to the user's trash folder
    
    if os.path.exists(trash_path):
        removed_files = glob.glob(trash_path + "/*")
        return removed_files
    else:
        print("Trash folder does not exist.")
        return []

def get_trash_files():
    trash_path = os.path.expanduser("~/.local/share/Trash/files")  # Path to the user's trash folder
    
    if os.path.exists(trash_path):
        files_in_trash = os.listdir(trash_path)
        return files_in_trash
    else:
        print("Trash folder does not exist.")
        return []

# Example usage
removed_files = get_removed_files()
if removed_files:
    print("Removed files:")
    for file in removed_files:
        print(os.path.basename(file))

trash_files = get_trash_files()
if trash_files:
    print("Files in Trash:")
    for file in trash_files:
        print(file)
