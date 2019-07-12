# python3
# instant_messenger_bot.py - automatically send out a notification
# message to friend.


import pyautogui


pyautogui.PAUSE = 1

friend_icon = pyautogui.locateOnScreen('friend.PNG')

if friend_icon:
    pyautogui.click(friend_icon)

    pyautogui.typewrite("Hello! I'm bot!", 0.2)
    pyautogui.press('enter')
else:
    print('The friend icon was not found!')
