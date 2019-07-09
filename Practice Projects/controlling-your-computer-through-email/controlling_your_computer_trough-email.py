#! python3
# controlling_your_computer_trough-email.py - Checks an email account for instructions.
# Executes instructions automatically.


import imapclient
import sys
import os
import email
import bs4
import subprocess

from email.header import decode_header

import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.disable(logging.DEBUG)


# log in to email server
imap_obj = imapclient.IMAPClient('imap.gmail.com')
imap_obj.login('ivanov.ivan.python.2019', 'mXiFHuYVHnQu')
imap_obj.select_folder('INBOX', readonly=True)

# fetch messages
messages = imap_obj.fetch(imap_obj.search(['SUBJECT', 'Instructions for execution']), 'RFC822')

for message_data in messages.values():

    email_message = email.message_from_bytes(message_data[b'RFC822'])

    payload = b''
    attachments = {}

    # merge multipart messages
    if email_message.is_multipart():

        parts = []
        for part in email_message.walk():

            content_type = part['Content-Type'].split(';')[0]
            if content_type in ('text/html', 'text/plain'):
                parts.append(part.get_payload(decode=True))
            elif content_type == 'application/octet-stream':
                filename = part.get_filename()
                if decode_header(filename)[0][1] is not None:
                    filename = decode_header(filename)[0][0].decode(decode_header(filename)[0][1])

                attachments[filename] = part.get_payload(decode=True)

        payload = b''.join(parts)

    else:
        payload = email_message.get_payload(decode=True)

    # get instructions
    soup = bs4.BeautifulSoup(payload, 'html.parser')
    instruction = soup.body.text

    # execute
    if instruction == 'Download torrent':
        for filename, content in attachments.items():
            open(filename, 'wb').write(content)
            if sys.platform == 'win32':
                subprocess.Popen(['C:\\Program Files\\qBittorrent\\qbittorrent.exe', os.path.basename(filename)])
            elif sys.platform == 'linux':
                print('Linux is not supported')
    else:
        print('Unknown instructions.')
        continue
