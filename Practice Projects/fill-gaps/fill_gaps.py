#! python3
# fill_gaps.py - Searches gaps in the numbering of files with
# a given prefix

import os
import re


def files_with_prefix(folder, prefix=''):

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

    if files is None:
        return []

    pattern = r'(\d)+'
    num_regex = re.compile(pattern)

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
            gaps_index.append(i-1)

    return gaps_index


def rename_files(files, index=0):

    if files is None:
        return []

    for filename in files[index:]:
        print(filename)
        # TODO: Rename file


target_folder = 'C:\\Users\\User\\Desktop\\github\\test'
target_prefix = 'spam'

searched_files = files_with_prefix(target_folder, target_prefix)
print(searched_files)

searched_gaps = gaps_in_files(searched_files, target_prefix)
print(searched_gaps)

rename_files(searched_files, searched_gaps[0])

#searched_files = files_with_prefix(target_folder, target_prefix)
#print(searched_files)
