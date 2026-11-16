from openpyxl import load_workbook
wb = load_workbook('10.21037atm-2020-57-1 (1vr).xlsx', read_only=True, data_only=True)
ws = wb['Table 1']
print('rows', ws.max_row, 'cols', ws.max_column)
header = [ws.cell(row=1, column=c).value for c in range(1, ws.max_column+1)]
print('header:', header)
for r in range(2, 8):
    print([ws.cell(row=r, column=c).value for c in range(1, ws.max_column+1)])
