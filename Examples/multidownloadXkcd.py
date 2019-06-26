#! python3
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests
import os
import bs4
import threading


os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd


def downloadXkcd(startComic, endComic):

    for urlNumber in range(startComic, endComic):
        # Download the page.
        pageUrl = 'https://xkcd.com/%s' % urlNumber
        print('Downloading page %s...' % pageUrl)
        try:
            res = requests.get(pageUrl)
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            print('Not Found for url: %s' % pageUrl)
            continue

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading the imgage %s...' % comicUrl)
            try:
                res = requests.get(comicUrl)
                res.raise_for_status()
            except requests.exceptions.HTTPError:
                print('Not Found for url: %s' % comicUrl)
                continue

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# Create and start the Tread objects.
downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
