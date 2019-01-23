import openpyxl, pprint, os


print('Opening workbook...')

wb = openpyxl.load_workbook(os.path.join(os.getcwd(), 'censuspopdata.xlsx'))
sheet = wb.get_sheet_by_name('Population by Census Tract')
print(type(sheet))
countyData = {}

print('Reading rows...')
# sheet.get_highest_row()
for row in range(2, int(sheet.max_row) + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

