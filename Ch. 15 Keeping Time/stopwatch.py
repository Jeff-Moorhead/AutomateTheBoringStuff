#! python3

import time
import pyperclip

lap = 0

print('Starting stop watch...')
while True:
    try:
        lap += 1
        start = time.time()
        input()
        end = time.time()
        print(f'Lap #{lap}: {str(round(end - start)).rjust(4)}s')
    except KeyboardInterrupt:
        print('Stopwatch stopped.')
        break
