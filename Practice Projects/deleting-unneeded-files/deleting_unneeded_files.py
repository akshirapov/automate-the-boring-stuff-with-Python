#! python3
# deleting_unneeded_files.py - Search large files or folders


import os

job_folder = os.path.join('/', 'home')
size = 100  # MB

for dir_path, dir_names, file_names in os.walk(job_folder):

    for dir_name in dir_names:
        path = os.path.join(dir_path, dir_name)
        dir_size = os.path.getsize(path)
        if dir_size > size * 1024 ** 2:
            print(os.path.abspath(path))

    for file_name in file_names:
        path = os.path.join(dir_path, file_name)
        file_size = os.path.getsize(path)
        if file_size > size * 1024 ** 2:
            print(os.path.abspath(path))
