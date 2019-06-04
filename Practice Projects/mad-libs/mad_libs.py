#! python
# mad_libs.py - Reads in text files and lets the user add
# their own text anywhere the [WORDS] appears in
# the text file

import re

replace_words = {
    'ADJECTIVE': '',
    'NOUN': '',
    'ADVERB': '',
    'VERB': ''
}

# Input
for k in replace_words.keys():
    replace_words[k] = input('Enter an ' + k + ':\n')

# Read
file = open('mad_libs_old.txt')
text = file.read()
file.close()

# Replace
for k, v in replace_words.items():
    regex = re.compile(k)
    text = regex.sub(v, text)

print(text)

# Write
file = open('mad_libs_new.txt', 'w')
file.write(text)
file.close()
