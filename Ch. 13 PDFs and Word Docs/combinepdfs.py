#! python3

import PyPDF2
import os

pdfs = list(filter(lambda file: file.endswith('.pdf'), os.listdir('.\\pdfs')))
pdfs.sort()

pdfWriter = PyPDF2.PdfFileWriter()

for file in pdfs:
    pdf = open(f'.\\pdfs\\{file}', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    if pdfReader.isEncrypted:
        continue

    for page in pdfReader.pages[1:]:
        pdfWriter.addPage(page)

output = open('mergedPDFs.pdf', 'wb')
pdfWriter.write(output)
output.close() 
