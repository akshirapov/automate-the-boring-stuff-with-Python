#! python3
# play2048.py - Opens the game 2048 and
# keeps sending up, right, down, and left keys

import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


game_over = ''
keys = {
    0: Keys.ARROW_UP,
    1: Keys.ARROW_RIGHT,
    2: Keys.ARROW_DOWN,
    3: Keys.ARROW_LEFT
}

# Open the game.
driver = webdriver.Firefox(executable_path='/home/alex/Downloads/geckodriver')
driver.get('https://play2048.co/')

# Play the game.
el_game = driver.find_element_by_css_selector('html')
while True:

    if game_over == 'Game over!':

        score = driver.find_element_by_css_selector('.score-container').text
        print(score)
        break

    el_game.send_keys(keys[random.randint(0, 3)])

    game_over = driver.find_element_by_css_selector('.game-container p').text
