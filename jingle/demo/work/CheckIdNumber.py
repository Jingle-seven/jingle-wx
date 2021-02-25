# coding: utf-8
# 每月已交农保计数统计

import openpyxl,os

def isErrorIdNumber(idNum):
    if not idNum or '身份证' in idNum: return False # 如果是空，视为正确身份证号码
    factor = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checkCode = [1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    idList = ["10" if x in ['X', 'x', 'Ⅹ'] else x for x in list(idNum)]
    sum = 0
    try:
        for i in range(17):
            sum = sum + int(idList[i]) * factor[i]
    except Exception as e:
        return True # 如果是不是数字，视为错误身份证号码
    if checkCode[sum % 11] == int(idList[17]): # 如果加和结果与最后一位校验码相同，说明是正确的身份证号码
        return False
    print('错误的身份证号：',idList,checkCode[sum % 11])
    return True

def isErrorBankNum(bankNum):
    if not bankNum or '银行' in bankNum: return False  # 如果是空或者表头，视为正确号码
    try: int(bankNum)
    except Exception as e:return True # 如果是不是数字，视为错误银行号码
    # 如果是这两种开头，不适用此校验规则，视为正确号码
    if bankNum[0:4] == '4405' or bankNum[0:4] == '6058': return False
    sum = 0
    for  i in range(len(bankNum)-1,-1,-1):
        orderFromLeft = len(bankNum) - i
        if orderFromLeft%2 == 0: #从右边数的顺序为偶数的位数，乘2
            a = int(bankNum[i]) * 2
            if a > 9 : a = a-9
            sum = sum + a
        else:
            sum = sum + int(bankNum[i])
    if sum %10 ==0:
        return False
    return True


xsl = openpyxl.load_workbook('C:/Users/Administrator/Desktop/农保/新农保开户/农保开户汇总表2020-2021.xlsx')
sheet = xsl['2021']
for row in sheet.values:
    if isErrorIdNumber(row[3]):
        print('身份证错',row[2],row[3])
    if isErrorBankNum(row[7]):
        print('银行卡错',row[2],row[3],row[7])