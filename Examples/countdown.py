#! python3
# countdown.py - A simple countdown script.

import time
import subprocess

print('Start!')

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end=',')
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file.
# subprocess.Popen(['start', 'alarm.wav'], shell=True)  # in Windows
subprocess.Popen(['see', 'alarm.wav'])  # in Linux
