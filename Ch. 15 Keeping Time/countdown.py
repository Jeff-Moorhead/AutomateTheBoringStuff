#! python3

import subprocess
import time

countdown = 10
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1

subprocess.Popen(['start', 'alarm.wav'], shell=True)
