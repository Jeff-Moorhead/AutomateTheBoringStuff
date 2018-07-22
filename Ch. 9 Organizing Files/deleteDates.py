# To delete unneeded example files from renameDates.py

import os
import re

fileRegex = re.compile(r"""^(.*?) #all text before date
((0|1)?\d)- #one or two digits for the month
((0|1|2|3)?\d)- #one or two digits for the day
((19|20)\d\d) #four digits for the year
(.*?)$ #all text after date
""", re.VERBOSE)

os.chdir('C:\\Users\\Jeff Moorhead\\Documents\\PythonScripts\\shutil_osPractice')
for file in os.listdir('.'):
    mo = fileRegex.search(file)

    if mo is None:
        continue

    os.unlink('.\\' + file)
