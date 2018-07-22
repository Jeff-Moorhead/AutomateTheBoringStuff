#! python3

# this is a practice program about the Collatz sequence
import sys, time


def collatz(number):  # defines how to get to the next term of the sequence

    if number % 2 == 0 and number != 0:  # if n is even
        return number // 2
    if number % 2 == 1:  # if n is odd
        return 3 * number + 1


print('''This is a Collatz sequence generator.
Type "help" for info or press enter to continue...''')

cont = input()  # allows user to ask for help or continue to program

if cont.lower() == 'help':  # prints info about sequence
    print('''The Collatz sequence is named after German mathematican, Lothar Collatz.
The sequence goes like this:

Start with any number n. If n is even, the next term is n/2. If n is odd,
the next term is 3n+1. This pattern continues until the sequence reaches n=1.

Collatz conjectured, but could not prove, that for any positive integer n,
the Collatz sequence will always reach 1.

The Collatz Conjecture is still unsolved.''')

    input('Press enter to continue...')  # continues to program

while True:
    length = 0  # initial length of sequence is defined to be 0
    try:
        n = input('Enter number (Or "stop" to exit): ')
        original = n  # program remembers original user input

        if n.lower() == 'stop':  # ends program
            break

        if int(n) == 0:  # forces input greater than 0
            print('0 is not a valid input.')
            continue

        while n != 1:  # starts sequence output for input n
            n = collatz(int(n))  # recursive use of n generates successive terms
            print(str(n), end='')
            # sys.stdout.write(str(n)) does the same thing
            time.sleep(.03)
            print('')
            length += 1  # adds 1 to length of sequence

        else:
            print('Length of sequence with n = ' + str(original) + ': ' + str(length))  # prints final length to screen
            continue  # asks for new input to generate a new sequence

    except ValueError:
        print('Input must be an integer. Please try again.')  # forces input to be integer value
        continue
