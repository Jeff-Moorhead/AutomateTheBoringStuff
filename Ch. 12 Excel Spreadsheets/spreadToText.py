#! python3

import openpyxl
import sys

wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb.active
index = 1

for column in sheet.columns:
    file = open(f'.\\textFiles\\column{index}.txt', 'w')
    for cell in column:
        if cell.value:
            file.write(cell.value)
    index += 1
    file.close()
