import os
import shutil
import win32com.client
from pathlib import Path
from collections import defaultdict

class ProPath:
    def __init__(self, desktop_path=None):
        self.desktop_path = desktop_path or Path.home() / 'Desktop'
        self.rules = defaultdict(list)
        self.shell = win32com.client.Dispatch("WScript.Shell")

    def add_rule(self, extension, folder_name):
        """Add a rule to organize files with a given extension into a specified folder."""
        self.rules[extension.lower()].append(folder_name)

    def organize_desktop(self):
        """Organize desktop icons based on user-defined rules."""
        for item in os.listdir(self.desktop_path):
            item_path = self.desktop_path / item
            if item_path.is_file():
                extension = item_path.suffix.lower()
                if extension in self.rules:
                    self.move_file(item_path, self.rules[extension][0])
            elif item_path.is_dir() and not self.is_system_folder(item):
                if item.lower() not in self.rules:
                    self.move_folder(item_path, "Folders")

    def move_file(self, file_path, folder_name):
        """Move a file to the specified folder."""
        target_folder = self.desktop_path / folder_name
        target_folder.mkdir(exist_ok=True)
        shutil.move(str(file_path), str(target_folder / file_path.name))

    def move_folder(self, folder_path, folder_name):
        """Move a folder to the specified folder."""
        target_folder = self.desktop_path / folder_name
        target_folder.mkdir(exist_ok=True)
        shutil.move(str(folder_path), str(target_folder / folder_path.name))

    def is_system_folder(self, folder_name):
        """Check if a folder is a system folder that should not be moved."""
        system_folders = ['Desktop', 'Documents', 'Downloads', 'Pictures', 'Music', 'Videos']
        return folder_name in system_folders

if __name__ == "__main__":
    propath = ProPath()
    propath.add_rule('.txt', 'Text Files')
    propath.add_rule('.jpg', 'Images')
    propath.add_rule('.png', 'Images')
    propath.add_rule('.docx', 'Documents')
    propath.add_rule('.xlsx', 'Spreadsheets')

    propath.organize_desktop()