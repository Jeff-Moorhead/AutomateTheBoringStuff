#! python3

# this is the practice project from Ch. 10 - Debugging

import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again.')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You suck at this game.')