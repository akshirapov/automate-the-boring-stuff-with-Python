#! python3
# sheduled_web_comic_downloader.py - Checks the websites of several web comics
# and downloads the images if the comic was updated since the last visit


import os
import requests
import bs4
from urllib.parse import urljoin

import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


def images_from_lunarbaboon():

    # Get site
    url = 'http://www.lunarbaboon.com/'
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Site %s can’t be reached. Status code: %s" % (url, response.status_code))
        return []

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div.body img')

    links = []
    for img in content:
        src = img['src'].split('?')[0]  # without options
        links.append(urljoin(url, src))

    return links


def download_images(images, folder):

    if not images:
        return

    os.makedirs(folder, exist_ok=True)

    for image_url in images:

        image_name = os.path.join(folder, os.path.basename(image_url))

        if os.path.isfile(image_name):
            continue

        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            continue

        image_file = open(image_name, 'wb')
        for chunk in response.iter_content(100000):
            image_file.write(chunk)
        image_file.close()


images1 = images_from_lunarbaboon()
folder1 = 'lunarbaboon'

download_images(images1, folder1)
