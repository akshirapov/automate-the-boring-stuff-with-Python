#!python3
# image_site_downloader.py - Downloads searched photos from image site

import os
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# Load photo-sharing site
geckodriver_path = '/home/alex/Downloads/geckodriver'

driver = webdriver.Firefox(executable_path=geckodriver_path)
driver.get('https://www.flickr.com')

# Search category of photos
el_search_field = driver.find_element_by_id('search-field')
el_search_field.send_keys('cats' + Keys.RETURN)

# Click photo first photo
el_photo_list = WebDriverWait(driver, 20). \
    until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "div.view.photo-list-view > div")))

el_photo = el_photo_list[0]

WebDriverWait(driver, 20). \
    until(expected_conditions.visibility_of(el_photo))

el_photo.click()

# Find the URL of the photo.
for i in range(20):

    el_main_photo = WebDriverWait(driver, 20). \
        until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "img.main-photo")))

    print(el_main_photo.get_attribute('id'))

    # Download the photo.
    try:
        url_photo = el_main_photo.get_attribute('src')
        print('Downloading image %s...' % url_photo)
        response = requests.get(url_photo)
        response.raise_for_status()
    except requests.exceptions.MissingSchema:
        # skip
        el_next = WebDriverWait(driver, 20). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a.navigate-target.navigate-next")))
        el_next.click()
        continue

    # Save the photo.
    os.makedirs('photos', exist_ok=True)

    photo_file = open(os.path.join('photos', os.path.basename(url_photo)), 'wb')
    for chunk in response.iter_content(100000):
        photo_file.write(chunk)
    photo_file.close()

    # Click next photo
    # el_next = driver.find_element_by_css_selector('a.navigate-target.navigate-next')
    el_next = WebDriverWait(driver, 20). \
        until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a.navigate-target.navigate-next")))
    el_next.click()

    sleep(5)
