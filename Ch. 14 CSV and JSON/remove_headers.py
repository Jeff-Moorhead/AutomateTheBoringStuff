#! python3

import csv
import os
import logging
import argparse

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logging.disable(logging.CRITICAL)
parser = argparse.ArgumentParser()
parser.add_argument('source', help='The directory to scan for csv readers. If -f option'
    + ' is passed, then source is a reader.')
parser.add_argument('-f', action='store_true', help='Set source to a reader name rather'
    + ' rather than a directory.')
args = parser.parse_args()

if args.f:
    lines = []
    file = open(args.source)
    reader = csv.reader(file)

    output = open('altered_' + args.source, 'w', newline='')
    writer = csv.writer(output)

    for line in reader:
        lines.append(line)
    
    logging.debug(f'Lines read: {len(lines)}')

    for line in lines[1:]:
        print(f'Copying line #{lines.index(line)}')
        writer.writerow(line)

    print('Header removed.')
    file.close()
    output.close()

else:
    csv_files = filter(lambda file: file.endswith('.csv'), os.listdir(args.source))
    for file in csv_files:
        print('Removing header from ' + file)
        lines = []
        current_file = open(f'{args.source}\\{file}')
        reader = csv.reader(current_file)

        output = open(args.source + '\\altered_files\\altered_' + file, 'w', newline='')
        writer = csv.writer(output)

        for line in reader:
            lines.append(line)
            
        logging.debug(f'Lines read: {len(lines)}')

        for line in lines[1:]:
            writer.writerow(line)

        print(f'Header removed from {file}')
        current_file.close()
        output.close()
