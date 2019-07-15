#! python3
# link_verification.py - Attempts to download linked pages on the page


import requests
import bs4
from urllib.parse import urljoin


url_base = 'https://automatetheboringstuff.com'

# Get the page
response = requests.get(url_base)
response.raise_for_status()

# Find all linked pages on the page
soup = bs4.BeautifulSoup(response.text, 'html.parser')
href_list = soup.select('[href]')

# Check pages
total = len(href_list)
for i, href in enumerate(href_list, 1):

    url_href = urljoin(url_base, href.get('href'))

    status = 'OK'
    try:
        response = requests.get(url_href, timeout=5)
        response.raise_for_status()
    except Exception:
        status = 'BROKEN'
    finally:
        print('[%s/%s] %s: %s' % (i, total, status, url_href))
