#! python3
# extending_resize_and_add_logo.py - Extends functionality for resizeAndAddLogo.py

"""
Extends:
3. Size of image should be twice of logo
"""

import os
from PIL import Image


SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_image = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_image.size

os.makedirs('with_logo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or
            filename.lower().endswith('.jpg') or
            filename.lower().endswith('.bmp') or
            filename.lower().endswith('.gif')) or \
            filename.lower() == LOGO_FILENAME.lower():
        continue  # skip non-image files and the logo file itself

    image = Image.open(filename)
    width, height = image.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % filename)
        image = image.resize((width, height))

    # Add the logo.
    if (width / logo_width < 2) or (height / logo_height < 2):
        print('Invalid size of origin image. Logo not has been added.')
    else:
        print('Adding logo to %s...' % filename)
        image.paste(logo_image, (width - logo_width, height - logo_height), logo_image)

    # Save changes.
    image.save(os.path.join('with_logo', filename))
