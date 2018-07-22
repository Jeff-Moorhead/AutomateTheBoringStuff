#! python3

# Selective Copier - Searches directory tree and copies desired file type to a new folder
"""Usage - search directory is the path of the directory tree you want to walk
filetype is the file extension you want to be copied (e.g. .pdf, .jpg, .docx)
destination is the path of the new folder you want the file matches to be copied to. This directory cannot
already exist so it must have a new name."""

import os
import shutil


def copier():
    directory = input('Enter search directory path: ')
    filetype = input('Enter file extension to search for: ')
    destination = input('Enter destination path for file copies: ')
    os.mkdir(destination)
    for folder, subfolders, files in os.walk(directory):
        print('Searching in ' + folder)
        print()

        for file in files:
            if file.endswith(filetype):
                try:
                    shutil.copy(os.path.join(folder, file), destination)
                    print(file + ' successfully moved to ' + destination)
                    print()
                    os.unlink(folder + '\\' + file)
                except shutil.SameFileError:
                    print(file + ' has already been moved to destination.')
                    continue


copier()
