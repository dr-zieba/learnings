from openpyxl.styles import *
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo


file_txt = open(r"C:\Users\zieba\Desktop\python\original.txt")

records = []
file_txt.seek(0)
print(file_txt.seek(0)
)

for record in file_txt.readlines():
    records.append(record.rstrip("\n").split(";"))

print(records)

print("Tworzniee xlsa")

workbook = Workbook()
file_path = r"C:\Users\zieba\Desktop\python\original_moj.xlsx"
workbook.save(file_path)

sheet = workbook['Sheet']
sheet.title = 'Employee'
workbook.save(file_path)

for row in records:
    sheet.append(row)

font = Font(color = colors.RED, bold = True, italic = True)

for cell in range(2,12):
    if int(sheet['G%s' % (cell)].value) > 55000:
        sheet['G%s' % (cell)].font = font

workbook.save(file_path)
file_txt.close()
