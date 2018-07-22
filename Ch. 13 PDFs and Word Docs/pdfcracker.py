#! python3

import PyPDF2
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

dictionary = open('dictionary.txt', 'r')
pdf = open('pdfs\\Syllabus_encrypted.pdf', 'rb')
logging.debug(pdf)
pdfReader = PyPDF2.PdfFileReader(pdf)
lines = dictionary.readlines()

logging.debug('Stripping line breaks...')
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n').lower()

logging.debug('Searching for password...')
for line in lines:
    logging.debug('Trying ' + line)
    if pdfReader.decrypt(line):
        print(f'The password was {line}.')
        sys.exit(0)

    
print('The PDF could not be cracked!')
