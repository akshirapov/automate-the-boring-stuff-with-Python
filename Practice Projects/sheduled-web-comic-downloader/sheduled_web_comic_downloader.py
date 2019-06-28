#! python3
# sheduled_web_comic_downloader.py - Checks the websites of several web comics
# and downloads the images if the comic was updated since the last visit


"""
Propose:
- Download images from several websites
- Check for updates
"""

import requests
import bs4
from urllib.parse import urljoin

import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


def download_from_lunarbaboon():

    # Get site
    url = 'http://www.lunarbaboon.com/'
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Site %s can’t be reached. Status code: %s" % (url, response.status_code))
        return

    # Get content
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Search elements with ref of image
    posts = soup.select('#content ')

    logging.debug(len(posts))

    for post in posts:
        logging.debug(post)

    last_post = posts[1]

    # logging.debug('\n' + last_post.prettify())


    # TODO: Check for the updates


    # TODO: Download image

download_from_lunarbaboon()
