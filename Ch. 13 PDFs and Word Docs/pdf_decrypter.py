#! python3

import PyPDF2
import os
import logging
import argparse


def decrypt_pdfs(file, password):
    if '_encrypted' in file:
        partition = file.partition('_encrypted.pdf')
    else:
        partition = file.partition('.pdf')
    pdf = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    if not pdfReader.isEncrypted:
        print(f'{file} is not encrypted.')
    else:
        pdfReader.decrypt(password)
        pdfWriter = PyPDF2.PdfFileWriter()
        pdfWriter.appendPagesFromReader(pdfReader)
        with open(partition[0] + '.pdf', 'wb') as copy:
            pdfWriter.write(copy)
            print('PDF successfully decrypted.')
    pdf.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.disable(logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=str, help='The folder to walk to decrypt PDFs.' +
    ' If -f is passed, then directory should be the path to an individual file to decrypt.')
    parser.add_argument('password', type=str, help='The password that decrypts the PDFs.')
    parser.add_argument('-f', action='store_true', help='Decrypt a single file.')
    args = parser.parse_args()
    logging.debug(f'Command line arguments: {args}')

    if args.f:
        print(f'Decrypting {args.directory}')
        decrypt_pdfs(args.directory, args.password)
    for folder, _, files in os.walk(args.directory):
        print(f'Working in folder {folder}')
        pdfs = filter(lambda file: file.endswith('.pdf'), files)
        for file in pdfs:
            try:
                decrypt_pdfs(f'{folder}\\{file}', args.password)
            except PyPDF2.utils.PdfReadError:
                print(f'Incorrect password for {file}!')
