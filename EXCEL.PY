import openpyxl as xl

wb=xl.load_workbook('VT LAB1 FINAL1.xlsx')
sheet = wb['Sheet1']
sheet['a1']
cell=sheet.cell(1,1)

print(cell.value)
