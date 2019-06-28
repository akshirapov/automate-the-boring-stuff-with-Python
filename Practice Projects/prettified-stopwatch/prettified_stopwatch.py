#! python3
# stopwatch.py - A simple stopwatch program.

import time
import pyperclip

# Display the program's instructions.
print('Press ENTER ot begin. Afterwards, press ENTER to "click" the stopwatch.'
      'Press Ctrl-C to quit.')
input()                     # press Enter to begin
print('Started.')
start_time = time.time()    # get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times.
try:
    text_to_clipboard = []
    while True:
        input()

        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)

        lap_num_str = ('Lap # %s:' % lap_num).ljust(9)
        total_time_str = (str(total_time) + ' (').rjust(6)
        lap_time_str = (str(lap_time) + ')').rjust(5)

        text = ' '.join((lap_num_str, total_time_str, lap_time_str))
        text_to_clipboard.append(text)

        print(text, end='')

        lap_num += 1
        last_time = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')

pyperclip.copy('\n'.join(text_to_clipboard))
