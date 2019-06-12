#! python3
# fill_gaps.py - Searches gaps in the numbering of files with
# a given prefix

import os
import re
import shutil


# target_folder = '/home/alex/test'
FOLDER = 'C:\\Users\\User\\Desktop\\github\\test'
PREFIX = 'spam'


def files_with_prefix(folder=FOLDER, prefix=PREFIX):

    files = []

    pattern = r'^%s(\d)+.txt' % prefix
    file_regex = re.compile(pattern, re.DOTALL)

    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            mo = file_regex.search(filename)
            if mo is not None:
                files.append(filename)
        break  # only top directory
    files.sort()

    return files


def gaps_in_files(files):

    if not files:
        return []

    num_regex = re.compile(r'(\d)+')

    gaps_index = []
    for i in range(len(files)):

        mo = num_regex.search(files[i])
        if mo is None:
            continue
        current_number = int(mo.group())

        if i == 0:
            last_number = current_number
        else:
            mo = num_regex.search(files[i-1])
            if mo is None:
                continue
            last_number = int(mo.group())

        diff = current_number - last_number
        if diff > 1:
            gaps_index.append(i)

    return gaps_index


def rename_files(files, index=0, folder=FOLDER, prefix=PREFIX):

    if not files:
        return

    num_regex = re.compile(r'((\d)+)')
    mo = num_regex.search(files[index-1])
    if mo is None:
        return

    number = int(mo.groups()[1])

    # temp folder for copies
    temp_folder = os.path.join(folder, 'temp')
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    for filename in files[index:]:

        number += 1

        new_filename = prefix + '{:03d}'.format(number) + '.txt'

        print('RENAME:', filename, '--->', new_filename)

        # move into temp folder
        src_path = os.path.join(folder, filename)
        dst_path = os.path.join(temp_folder, new_filename)
        shutil.move(src_path, dst_path)

    # move copies from temp folder
    for copy_filename in os.listdir(temp_folder):

        src_path = os.path.join(temp_folder, copy_filename)
        shutil.move(src_path, folder)

    if os.path.exists(temp_folder):
        os.rmdir(temp_folder)


def insert_gaps(files, gaps, folder=FOLDER, prefix=PREFIX):

    if not files:
        return

    if not gaps:
        return

    num_regex = re.compile(r'((\d)+)')
    mo = num_regex.search(files[0])
    if mo is None:
        return

    number = int(mo.groups()[1])

    # temp folder for copies
    temp_folder = os.path.join(folder, 'temp')
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    for i in range(len(files)):

        if i in gaps:
            number += 1

        filename = files[i]
        new_filename = prefix + '{:03d}'.format(number) + '.txt'

        # move into temp folder
        src_path = os.path.join(folder, filename)
        dst_path = os.path.join(temp_folder, new_filename)
        shutil.move(src_path, dst_path)

        number += 1

    # move copies from temp folder
    for copy_filename in os.listdir(temp_folder):

        src_path = os.path.join(temp_folder, copy_filename)
        shutil.move(src_path, folder)

    if os.path.exists(temp_folder):
        os.rmdir(temp_folder)


print('FILES:')
searched_files = files_with_prefix()
print(searched_files)

print('INDEXES OF GABS:')
searched_gaps = gaps_in_files(searched_files)
print(searched_gaps)

if searched_gaps:
    rename_files(searched_files, searched_gaps[0])

print('FILES:')
searched_files = files_with_prefix()
print(searched_files)

print('INSERT GAPS:')
gaps = [2, 5, 10]  # indexes of gaps
insert_gaps(searched_files, gaps)
