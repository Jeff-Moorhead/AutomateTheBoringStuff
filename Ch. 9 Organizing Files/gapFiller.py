#! python3

# Gap Filler - finds gaps in file numbering and fills them in
# Only works if gap is not larger than 2

import os
import shutil

searchFolder = input('Enter folder to search: ')
prefix = input('Enter prefix to search for: ')
fileType = input('Enter file extension to search for: ')

i = 0
for file in os.listdir(searchFolder):
    if os.path.exists(os.path.join(searchFolder, prefix + '%d' % i + fileType)):
        print('File found: ' + prefix + '%d' % i + fileType)
        i += 1
        continue

    else:
        try:
            print('File not found: ' + prefix + '%i' % i + fileType)
            shutil.move(os.path.join(searchFolder, prefix + '%d' % (i + 1) + fileType),
                        os.path.join(searchFolder, prefix + '%d' % i + fileType))
            print('Gap filled')
            i += 1
            continue
        except FileNotFoundError:
            shutil.move(os.path.join(searchFolder, prefix + '%d' % (i + 2) + fileType),
                        os.path.join(searchFolder, prefix + '%d' % i + fileType))
            print('Gap filled.')
            i += 1

    print('Done.')
