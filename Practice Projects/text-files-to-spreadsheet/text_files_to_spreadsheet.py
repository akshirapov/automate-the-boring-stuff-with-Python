#! python3
# text_files_to_spreadsheet.py - Saves text of each files to separate column.
# line to row


import openpyxl

files = [
    'text_1.txt',
    'text_2.txt',
    'text_3.txt'
]


texts = []

for filename in files:
    file = open(filename)
    texts.append(file.readlines())
    file.close()


wb = openpyxl.Workbook()
sheet = wb.active


for i in range(len(texts)):
    for j in range(len(texts[i])):
        sheet.cell(row=j+1, column=i+1).value = texts[i][j].strip()

wb.save('texts.xlsx')
print('Done.')
