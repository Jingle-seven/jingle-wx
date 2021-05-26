# coding: utf-8
# 每月已交农保计数统计

import openpyxl,os

dir = 'C:/Users/Administrator/Desktop/市局发文/关于统计辖区内人力资源状况的通知/水口各村/'
fileNameList = os.listdir(dir)
print(fileNameList)
def isError(sheet, sumCell, *factorCells):
    sum = sheet[sumCell].value
    factorCellsSum = 0
    for c in factorCells:
        # print(type(sheet[c].value))
        if not type(sheet[c].value) == int:
            continue
        factorCellsSum = factorCellsSum + sheet[c].value
    if sum == factorCellsSum:
        return False
    else:
        print(sumCell+'的值为'+str(sum),'不等于：'+str(factorCellsSum),end=' ')
        return True

for f in fileNameList:
    if not f.endswith('xlsx') or f.startswith('~$'):
        continue
    xsl = openpyxl.load_workbook(dir + f)
    sheet = xsl.worksheets[0]
    correct = True
    if isError(sheet, 'c8', 'd8', 'e8'):
        correct = False
    if isError(sheet, 'f8', 'g8', 'h8'):
        correct = False
    if  isError(sheet, 'h8', 'i8', 'j8'):
        correct = False
    if isError(sheet, 'l8', 'm8', 'n8', 'o8'):
        correct = False
    if sheet['h8'].value < sheet['k8'].value + sheet['l8'].value:
        print('劳动力人数小于务工务农人数',end='')
        correct = False
    if sheet['o8'].value < sheet['p8'].value:
        print('县内务工人数小于镇内务工人数',end='')
        correct = False
    if not correct:
        print(f,'error')

print("检查完成")