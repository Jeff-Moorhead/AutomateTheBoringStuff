#! python3

import openpyxl
import sys

wb = openpyxl.load_workbook(sys.argv[3])
sheet = wb.active
index = int(sys.argv[1])
count = int(sys.argv[2])

sheet.insert_rows(idx=index, amount=count)
wb.save('insertedRows.xlsx')
