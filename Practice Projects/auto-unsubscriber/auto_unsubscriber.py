# python3
# auto_unsubscriber.py - Finds all the unsubscribe links in emails,
# and automatically opens them in a browser.

import imapclient
import sys
import email
import bs4
import webbrowser


unsubscribe_links = []

# log in to email server
imap_obj = imapclient.IMAPClient('imap.gmail.com')
imap_obj.login('ivanov.ivan.python.2019', sys.argv[1])
imap_obj.select_folder('INBOX', readonly=True)

# fetch messages
messages = imap_obj.fetch(imap_obj.search('ALL'), 'RFC822')

for uid, message_data in messages.items():
    email_message = email.message_from_bytes(message_data[b'RFC822'])
    payload = b''

    # merge multipart messages
    if email_message.is_multipart():
        parts = []
        for part in email_message.walk():
            content_type = part['Content-Type'].split(';')[0]
            if content_type in ('text/html', 'text/plain'):
                parts.append(part.get_payload(decode=True))
        payload = b''.join(parts)

    # search unsubscribe link
    soup = bs4.BeautifulSoup(payload, 'html.parser')
    tags_a = soup.find_all('a', string='Unsubscribe')  # for simplicity search only 'Unsubscribe'
    for tag in tags_a:
        unsubscribe_links.append(tag['href'])

# open unsubscribe links
for url in unsubscribe_links:
    webbrowser.open(url)
