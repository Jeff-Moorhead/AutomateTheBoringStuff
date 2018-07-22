#! python3

# backUptoZip - Backs up a folder and its contents to a ZIP file

import zipfile
import os


def backupToZip(folder):
    # Backup the contents of a folder into a ZIP file.

    folder = os.path.abspath(folder)  # make sure folder path is absolute
    number = 1

    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
