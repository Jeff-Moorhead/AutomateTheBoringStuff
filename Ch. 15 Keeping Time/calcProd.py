#! python3

# calcProd.py - calculate the product of the first 100,000 integers.
import time


def calc_prod():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product


startTime = time.time()
product = calc_prod()
endTime = time.time()
print('The result is %s digits long.' % len(str(product)))
print('Took %s seconds to calculate.' % (endTime - startTime))
