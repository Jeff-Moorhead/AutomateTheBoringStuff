#! python3

import threading
import time
print('-----Start of program-----')


def take_a_nap():
        time.sleep(5)
        print('Hello world!')


def multiplier(n, m):
        return n * m


thread = threading.Thread(target=take_a_nap)
thread.start()

mult_thread = threading.Thread(target=multiplier, args=(2, 5))
product = mult_thread.start()

print('-----End of program-----')
