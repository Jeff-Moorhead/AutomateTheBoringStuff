#! python3
# mapIt.py - launches Google Maps to a desired address

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('www.google.com/maps/place/' + address)
