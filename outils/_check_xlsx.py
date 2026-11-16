from openpyxl import load_workbook
files = ['10.21037atm-2020-57-1.xlsx','10.21037atm-2020-57-1 copy.xlsx','10.21037atm-2020-57-1 (1vr).xlsx']
for f in files:
    try:
        wb = load_workbook(f, read_only=True, data_only=True)
        print(f, 'OK', wb.sheetnames)
    except Exception as e:
        print(f, 'ERROR', type(e).__name__, str(e)[:180])
