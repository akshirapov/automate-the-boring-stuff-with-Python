#! python3
# bf_pdf_password_breaker.py - Decrypts the PDF by Brute-Force method

import PyPDF2


words = open('dictionary.txt').readlines()

pdf_reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

for word in words[:5]:

    password = word.strip().lower()
    if pdf_reader.decrypt(password):
        print('Success! Password:', password)
        break

    password = word.strip().upper()
    if pdf_reader.decrypt(password):
        print('Success! Password:', password)
        break
