#! python3
# looking_busy.py - Nudges mouse cursor slightly every ten seconds.

import pyautogui
import time

while True:
    pyautogui.moveRel(10, 0)
    pyautogui.moveRel(-10, 0)
    time.sleep(10)
