# coding=utf-8
import difflib

filePath = "../resource/jieba/真心话问题.txt"
resFilePath = "../resource/jieba/真心话问题res.txt"
# 写文件
resFile = open(resFilePath, "w", encoding="utf-8")

def compareStr(str1,str2):
    str2 = str2.strip()
    str1 = str1.strip()
    if len(str2) == 0 or len(str1) == 0:
        return 0
    counter1 = 0
    counter2 = 0
    for i in str1:
        if str2.find(i) >-1:
            counter1 = counter1 +1
    for i in str2:
        if str1.find(i) >-1:
            counter2 = counter2 +1
    num1 = round((counter1/len(str1))*100)
    num2 = round((counter2/len(str2))*100)
    # print(str1,'|'+str2,num1,num2)
    return num1 if num1 <num2 else num2

# 读文件
# 默认第二个参数为r,file = open("G:/temp/test.txt","r")
file = open(filePath,encoding="utf-8")
lines = file.readlines()
l2 = lines.copy()
lineDict = {'example':[]}
i = 0
while i < len(lines):
    line = lines[i]
    noOneSimilar = True # 如果遍历完整个lineDict都没找到相似句子的话，把这个新句子列入lineDict
    print(i,lines)
    print(line)
    for k in list(lineDict.keys()):
        if compareStr(k, line) > 70:
            lineDict[k].append(line)
            noOneSimilar = False
            lines.pop(i)
            i = i - 1
            break
    i = i+1
    if noOneSimilar:
        lineDict[line] = []
    else:
        noOneSimilar = True

i = 0
for k,v in lineDict.items():
    i = i+ 1
    resFile.write(str(i) +'.'+ str(k).strip() + repr(v).replace('\\n',''))
    resFile.write('\n')
file.close()
resFile.close()



# print(compareStr('你喜欢谁?\n','\n'))
