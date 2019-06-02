#! python
# strong-password-detection.py - Make sure the password string it is passed
# is strong.

import re


def strong_password(check_password):

    if check_password == '':
        print('Password can not be empty.')
        return False

    len_regex = re.compile(r'.{8,}')
    upper_case_regex = re.compile(r'[A-Z]+')
    low_case_regex = re.compile(r'[a-z]+')
    num_regex = re.compile(r'\d')

    if len_regex.search(check_password) is None:
        print('Password must be at least eight characters long.')
        return False
    if upper_case_regex.search(check_password) is None:
        print('Password must contain both uppercase and lowercase characters.')
        return False
    if low_case_regex.search(check_password) is None:
        print('Password must contain both uppercase and lowercase characters.')
        return False
    if num_regex.search(check_password) is None:
        print('Password must have at least one digit.')
        return False
    print('Password is strong.')
    return True


password = input("Enter password: ")

strong_password(password)
