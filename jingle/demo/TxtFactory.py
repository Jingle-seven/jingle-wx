# coding=utf-8
import difflib

filePath = "../resource/jieba/真心话问题.txt"
resFilePath = "../resource/jieba/真心话问题res.txt"
# 写文件
resFile = open(resFilePath, "w", encoding="utf-8")

def compareStr(str1,str2):
    str2 = str2.strip()
    if len(str2) == 0:
        return 0
    counter = 0
    print(repr(str1),repr(str2))
    for i in str2:
        if str1.find(i) >-1:
            counter = counter +1
    return round((counter/len(str2))*100)

# 读文件
# 默认第二个参数为r,file = open("G:/temp/test.txt","r")
file = open(filePath,encoding="utf-8")
lines = file.readlines()[0:5]
l2 = lines.copy()
lineDict = {'example':[]}

for i in lines:
    for k in list(lineDict.keys()):
        if compareStr(k,i) > 70:
            # print(repr(k),repr(i),compareStr(k,i))
            lineDict[k].append(i)
        else:
            lineDict[i] = []
    lineDict[i] = []

print(len(lineDict))
for k,v in lineDict.items():
    resFile.write(str(k))
    resFile.write(repr(v))
    resFile.write('\n')
file.close()
resFile.close()



# print(compareStr('你喜欢谁?\n','\n'))
