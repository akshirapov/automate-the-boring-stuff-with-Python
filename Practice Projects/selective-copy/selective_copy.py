#! python3
# selective_copy.py - Copies files with specific extension

import os
import shutil


job_folder = os.path.join('/', 'home', 'alex', 'github', 'automate-the-boring-stuff')
copy_folder = os.path.join('/', 'home', 'alex', 'github', 'automate-the-boring-stuff', 'copy-folder')

for folder, sub_folders, files in os.walk(job_folder):

    for file in files:
        if file.endswith('.pdf'):
            shutil.copy(os.path.abspath(os.path.join(folder, file)), copy_folder)
