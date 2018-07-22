#! python3

import os


def filefinder():
    largeFiles = []
    tree = input('Enter directory path to search for large files in: ')
    searchSize = int(input('Search for files larger than (1024 bytes = 1 kilobyte): '))
    for folder, subfolders, files in os.walk(tree):
        # print('Searching in ' + folder)

        for file in files:
            if os.path.getsize(os.path.join(folder, file)) > searchSize:
                # print(os.path.basename(file) + 'has a size of ' + str(os.path.getsize(os.path.join(folder, file))))
                largeFiles.append(file)
                fileSize = os.path.getsize(os.path.join(folder, file))
                continue
        for file in largeFiles:
            print('Large file found :' + os.path.join(folder, file) + '(' + str(fileSize) + ' bytes)')
    if len(largeFiles) == 0:
        print('Could not find files large than ' + str(searchSize) + ' bytes.')
    else:
        print('Number of large files found: ' + str(len(largeFiles)))


filefinder()