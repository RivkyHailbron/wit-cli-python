import filecmp
import json
import os
import shutil
from fileinput import close

from Commit import Commit
from colorama import init, Fore

init(autoreset=True)


def create_file(path):
    if not os.path.exists(path):
        with open(path, 'w'):
            pass


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Folder {path}created!")
    else:
        print(f"Folder {path} already exists")


def copy_file(source_file, destination_file):
    if os.path.exists(source_file):
        shutil.copyfile(source_file, destination_file)
    else:
        e = f"The file {source_file} does not exist."
        raise ValueError(e)


def copy_folder(source_folder, destination_folder):
    if os.path.exists(source_folder):
        shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)


def copy_folder_contents(source_folder, destination_folder):
    # Check if the folder exists
    if os.path.exists(source_folder) and os.path.exists(destination_folder):
        for item in os.listdir(source_folder):
            item_path = os.path.join(source_folder, item)
            # Check if it's a file or directory and copy accordingly
            if os.path.isfile(item_path):
                copy_file(item_path, item_path)  # copy file
            elif os.path.isdir(item_path) and item != '.wit':
                shutil.copytree(item_path, os.path.join(destination_folder, item_path),dirs_exist_ok=True)  # copy directory and its contents
    else:
        raise ValueError(f"The {source_folder} folder does not exist.")


def delete_folder_contents(folder_path):
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Iterate over the contents of the folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            # Check if it's a file or directory and delete accordingly
            if os.path.isfile(item_path):
                os.remove(item_path)  # Remove file
            elif os.path.isdir(item_path) and item != '.wit':
                shutil.rmtree(item_path)  # Remove directory and its contents
    else:
        raise ValueError(f"The {folder_path} folder to delete does not exist.")


def filter_stage(stage_folder, project_folder):
    # קבלת רשימת הקבצים בתיקיית היעד
    project_files = set(os.listdir(project_folder))
    # מעבר על כל הקבצים בתיקיית המקור
    for filename in os.listdir(stage_folder):
        # אם הקובץ לא נמצא בתיקיית היעד, נמחק אותו
        if filename not in project_files:
            file_path = os.path.join(stage_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")


# src = project folder des=stage folder
def compare_files(source_folder, destination_folder):
    if os.path.exists(source_folder) and os.path.exists(destination_folder):
        files = os.listdir(source_folder)
        for f in files:
            if f != '.wit':
                source_file_path = os.path.join(source_folder, f)
                destination_file_path = os.path.join(destination_folder, f)
                if not os.path.exists(destination_file_path):
                    # קבצים שאינם במעקב
                    print(Fore.YELLOW + f"\t File {f} is untracked in stage area.\n")
                else:
                    if not filecmp.cmp(source_file_path, destination_file_path):
                        # Files were changed but not added.
                        print(Fore.RED + f"\t File {f} is modified .\n")
                    else:
                        # Files prepared for commit
                        print(Fore.GREEN + f"\t File {f} is stage.\n")
#print(Fore.YELLOW+"hello")
#print(Fore.RED+"hello")