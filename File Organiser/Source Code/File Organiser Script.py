import os
import shutil
import argparse

def create_subfolder(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def move_file(file_path, subfolder_path):
    shutil.move(file_path, subfolder_path)

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                move_file(file_path, subfolder_path)
                print(f"Moved: {filename} -> {subfolder_name}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organise files by extension type')
    parser.add_argument('folder_path', help='Path to the folder you want to organise')
    args = parser.parse_args()
    
    if os.path.isdir(args.folder_path):
        clean_folder(args.folder_path)
        print("Cleaning complete.")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again.")
