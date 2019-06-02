#! python
# regex_version_of_strip.py - Takes a string and does the same thing
# as the strip()

import re


def like_strip(string, chars=''):

    regex_str = r'(\s)'

    if chars is None:
        regex_str = r'^(\s+)|(\s+)$'

    regex = re.compile(regex_str)
    return regex.sub(chars, string)


text = ' \t\n Hello, Alex! \t\n'

strip_text = like_strip(text)
print(strip_text)
