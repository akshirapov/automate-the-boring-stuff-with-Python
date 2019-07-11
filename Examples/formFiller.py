#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time

import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'amulet',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]

# Set these to the correct coordinates for your computer.
nameField = (1040, 457)
submitButton = (1040, 900)
submitButtonColor = (26, 115, 232)
submitAnotherLink = (1070, 365)

pyautogui.PAUSE = 0.5

for person in formData:
    # Give the user a chance to kill script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(5)

    print('Entering %s info...' % person['name'])
    pyautogui.click(nameField[0], nameField[1])

    # Fill out the Name Field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', 'enter', '\t'], 0.2)
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', 'enter', '\t'], 0.2)
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'], 0.2)
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'], 0.2)
    else:
        pyautogui.typewrite(['down', 'enter', '\t'], 0.2)

    pyautogui.typewrite('\t')

    # Fill out the Robocop field.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'], 0.2)
    if person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'], 0.2)
    if person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'], 0.2)
    if person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'], 0.2)
    if person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'], 0.2)

    # Fill out the Additional Comments field.
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Sumbit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
