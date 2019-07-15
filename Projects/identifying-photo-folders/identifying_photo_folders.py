#! python3
# identifying_photo_folders.py - Scans the entire hard drive and finds
# photo folders.Photo folders is that it's any folder, where more than
# half of the files are photos.

import os
from PIL import Image


for root, dirs, files in os.walk('/home'):
    num_photo_files = 0
    num_non_photo_files = 0

    for filename in files:
        # Check file extension
        if not (filename.endswith('.jpg') or filename.endswith('.png')):
            num_non_photo_files += 1
            continue  # skip to next filename

        # Open image file
        image = Image.open(os.path.join(root, filename))
        width, height = image.size

        # Check size
        if width > 500 and height > 500:
            num_photo_files += 1
        else:
            num_non_photo_files += 1

    # Check for "photo" folder.
    if num_photo_files > num_non_photo_files:
        print(os.path.abspath(root))
