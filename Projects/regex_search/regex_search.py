#! python
# regex_search.py - Opens all .txt files in a folder and searches
# for any line that matches a user-supplied regular expression.

import os
import re

folder = os.getcwd()

# Find all .txt files
pattern = r'.+\.txt'
regex = re.compile(pattern)

files = []
for content in os.listdir(folder):
    mo = regex.search(content)
    if mo is not None:
        files.append(content)

# Search any line that matches a user regex
pattern = input('Enter regex: \n')
regex = re.compile(pattern)

for file_name in files:

    file = open(os.path.join(folder, file_name))
    list_txt = file.readlines()
    file.close()

    for line in list_txt:
        mo = regex.search(line)
        if mo is not None:
            print(line)
