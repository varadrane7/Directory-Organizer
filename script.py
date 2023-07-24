import os
import shutil
from tkinter import filedialog
from tkinter import Tk

def main():
    # Initialize tkinter
    root = Tk()
    root.withdraw()

    # Open folder dialog
    folder_path = filedialog.askdirectory()

    if not folder_path:
        print("No folder selected. Exiting...")
        return

    # Define file types
    file_types = {
        'docs': ['.doc', '.docx', '.txt', '.pdf'],
        'excel': ['.xls', '.xlsx', '.csv'],
        'powerpoint': ['.ppt', '.pptx'],
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.ico'],
        'programs': ['.exe', '.sh', '.bat', '.jar'],
        'compressed': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'other': []
    }

    # Create folders for each file type
    for folder, _ in file_types.items():
        if not os.path.exists(os.path.join(folder_path, folder)):
            os.mkdir(os.path.join(folder_path, folder))

    # Iterate over files and move them to corresponding folders
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)

        # Find which folder this file should go into
        for folder, extensions in file_types.items():
            if extension in extensions:
                destination_folder = os.path.join(folder_path, folder)
                shutil.move(file_path, destination_folder)
                break
        else:
            # If no match is found, move to 'other'
            other_folder = os.path.join(folder_path, 'other')
            shutil.move(file_path, other_folder)

    print("Files organized successfully.")

if __name__ == "__main__":
    main()
