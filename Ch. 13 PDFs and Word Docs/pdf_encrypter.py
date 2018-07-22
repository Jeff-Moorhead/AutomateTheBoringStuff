#! python3

"""Encrypt PDF files in a directory tree using a password provided
as a command-line argument. Once each file has been encrypted, it
is deleted. The first command-line argument is the path to the 
base folder and the second is the password to encrypt the pdf files 
with."""

import PyPDF2
import os
import logging
import argparse


def encrypt_pdf(file, password):
    new_file_name = file.partition('.pdf')[0] + '_encrypted.pdf'
    logging.debug('New file name: %s' % new_file_name)
    with open(file, 'rb') as pdf:
        pdfReader = PyPDF2.PdfFileReader(pdf)
        
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.appendPagesFromReader(pdfReader)
        pdfWriter.encrypt(password)
        base = open(new_file_name, 'wb')
        pdfWriter.write(base)
        base.close()

    return PyPDF2.PdfFileReader(open(new_file_name, 'rb'))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.disable(logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='The directory to walk. If -f is passed,'
    + ' then directory should be a single file to be encrypted.', type=str)
    parser.add_argument('password', help='The password to decrypt PDFs.', type=str)
    parser.add_argument('-f', action='store_true', help='Encrypt a single file.')

    args = parser.parse_args()

    base = args.directory
    password = args.password

    if args.f:
        logging.debug('-f was passed as an argument.')
        encrypt_pdf(base, password)
    else:
        for folder, _, files in os.walk(base):
            print('Working in folder %s' % folder)
            pdfs = filter(lambda file: file.endswith('.pdf'), files)
            for file in pdfs:
                try:
                    logging.debug(f'{folder}\\{file}')
                    encrypted_pdf = encrypt_pdf(f'{folder}\\{file}', password)
                    assert encrypted_pdf.isEncrypted
                    if encrypted_pdf.decrypt(password):
                        print('File encrypted successfully.\n')
                        os.remove(f'{folder}\\{file}')
                except PyPDF2.utils.PdfReadError:
                    print(f'{file} is already encrypted!\n')
                    continue
