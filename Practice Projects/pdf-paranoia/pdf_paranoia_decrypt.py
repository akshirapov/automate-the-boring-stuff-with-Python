#! python3
# pdf_paranoia_encrypt.py - Encrypts the PDFs using a password


import sys
import os
import PyPDF2

import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s -- %(message)s')


def decrypt_files(files, password=''):

    for filename in files:

        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        if not pdf_reader.isEncrypted:
            continue

        if pdf_reader.decrypt(password) == 0:
            print('Incorrect password!', filename, 'has not been decrypted.')
            continue

        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        filename_new = os.path.splitext(filename)[0].split('_')[0] + '.pdf'
        pdf_file_new = open(filename_new, 'wb')

        pdf_writer.write(pdf_file_new)
        print('New decrypted file:', pdf_file)

        pdf_file.close()
        pdf_file_new.close()


password = '123'
if len(sys.argv) >= 2:
    password = sys.argv[1]

pdf_list = []
for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.pdf'):
            pdf_list.append(os.path.join(root, filename))

decrypt_files(pdf_list, password)
