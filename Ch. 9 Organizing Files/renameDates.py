# Program to extract dates and reformat to European style dd-mm-yyyy - Automate the Boring Stuff Ch. 9

import os, shutil, re
# Create a regex to match American-style dates

datePattern = re.compile(r"""^(.*?) #all text before date
((0|1)?\d)- #one or two digits for the month
((0|1|2|3)?\d)- #one or two digits for the day
((19|20)\d\d) #four digits for the year
(.*?)$ #all text after date
""", re.VERBOSE)

# Groups are numbered by open parentheses

# Loop over files in CWD
os.chdir(r'C:\Users\Jeff Moorhead\Documents\PythonScripts\shutil_osPractice')
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the file name
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style file name
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths
    absWorkDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkDir, amerFilename)
    euroFilename = os.path.join(absWorkDir, euroFilename)

    # Rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)


