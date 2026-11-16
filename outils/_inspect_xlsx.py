from openpyxl import load_workbook
from pathlib import Path
p = Path('10.21037atm-2020-57-1.xlsx')
wb = load_workbook(p, read_only=True, data_only=True)
print('sheets:', wb.sheetnames)
for s in wb.sheetnames:
    ws = wb[s]
    max_row = ws.max_row
    max_col = ws.max_column
    print(f'\n[{s}] rows={max_row} cols={max_col}')
    header = [ws.cell(row=1, column=c).value for c in range(1, max_col+1)]
    print('header:', header)
    for r in range(2, min(7, max_row+1)):
        row = [ws.cell(row=r, column=c).value for c in range(1, max_col+1)]
        print(row)
