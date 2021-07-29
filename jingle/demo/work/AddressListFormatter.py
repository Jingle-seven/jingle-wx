# coding: utf-8
# 通讯录补空

import time,openpyxl
fileName = 'C:/Users/Administrator/Desktop/txl.xlsx'

book = openpyxl.load_workbook(fileName)
sheet = book['Sheet1']
dept = None
name = None
# 填充空白并合并部门和姓名
for rowNum in range(2,sheet.max_row+1):

    deptCell = sheet.cell(rowNum, 1)
    nameCell = sheet.cell(rowNum, 2)
    if deptCell and deptCell.value:
        dept = deptCell.value
    if nameCell and nameCell.value:
        name = nameCell.value
    sheet.cell(rowNum, 4).value = '水口镇' + dept + name

    print(dept,name,)
book.save(fileName)