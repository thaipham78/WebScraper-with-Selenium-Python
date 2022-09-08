import csv


def csv_WriteHeaderData(fileName, collumnData):
    with open(fileName, 'a', encoding='UTF8', newline='') as f:
        csvWriter = csv.DictWriter(f, fieldnames=collumnData)
        csvWriter.writeheader()


"""
Call this to set up collum in csv
"""
# file = 'sample.csv'
# collums = ['Product Name', 'Product Price', 'Date', 'Source']
# csv_WriteHeaderData(file,collums)


def csv_WriteRowData(fileName, collumnData, rowData):
    with open(fileName, 'a', encoding='UTF8', newline='') as f:
        csvWriter = csv.DictWriter(f, fieldnames=collumnData)
        csvWriter.writerows(rowData)
