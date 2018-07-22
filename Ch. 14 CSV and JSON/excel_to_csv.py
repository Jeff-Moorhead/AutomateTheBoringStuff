#! python3

import openpyxl
import csv
import os
import argparse
import logging

logging.disable(logging.CRITICAL)


def extract_cell_values(row):
    values = []
    for cell in row:
        values.append(cell.value)
    return values


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')

    excel_files = filter(lambda file: file.endswith('.xlsx'), os.listdir())
    os.mkdir('converted_csv')
    
    for file in excel_files:
        print('Converting workbook...')
        wb = openpyxl.load_workbook(file)

        for sheet in wb.worksheets:
            with open('converted_csv\\' + sheet.title + '_csv.csv', 'w', 
                newline='') as output:
                writer = csv.writer(output)
                for row in sheet.rows:
                    writer.writerow(extract_cell_values(row))
