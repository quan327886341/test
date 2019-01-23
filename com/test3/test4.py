import openpyxl, os
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.getcwd())
url = os.path.join(os.getcwd(), 'example.xlsx')
print(url)
wb = openpyxl.load_workbook(url)
print(type(wb))
print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet1')
print(sheet['A1'].value)