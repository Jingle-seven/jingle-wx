# coding: utf-8

# print(int("ff", 16))
# print(oct(894))
# print(bin(789))
# print(hex(1490327531782603538)[2:])
# print(len(hex(1 << 128)))
# str = '123456789'
# print(str[:3])
#s = input("请输入代码： ")
# print('10' in str)
# print({}.update(None))
# a = [1,2,3] #index 0,1,2
# a.insert(3,'x')
# print(a)
# s = '123456789'
# print(s.replace('1','').replace('2',''))
# s = ['a','b','c','d','e',]
# for i in range(0,len(s)):
#     print(i)
# for i in s:
#     if i == 'c' or i == 'b' :
#         s.pop()
#     print(i)
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

isErrorIdNumber('440223199408300516')