#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press ENTER ot begin. Afterwards, press ENTER to "click" the stopwatch.'
      'Press Ctrl-C to quit.')
input()                     # press Enter to begin
print('Started.')
startTime = time.time()     # get the first la's start time
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
