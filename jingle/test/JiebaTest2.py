import jieba
import jieba.posseg as psg
import jieba.analyse
from collections import Counter

txt = open('../resource/jieba/真心话问题.txt',encoding='utf8').read()

#词
words = list(jieba .cut(txt))
# print([x for x in words])

#词和词性
# print([x for x in psg .cut(txt)])
i = 0
while i<len(words):
    print(i,words[i],words[:10])
    if len(words[i])==1:
        words.pop(i)
        i = i-1
    i = i+1
print(words)
#出现最多的几个词(还待去除停止词)
c = Counter(words).most_common(50)
print(c)

# 自定义停止词和语料库
jieba.analyse.set_stop_words("../resource/jieba/stop_words.txt")
# jieba.analyse.set_idf_path("../extra_dict/idf.txt.big")
#关键词
# tags = jieba.analyse.extract_tags(txt, topK=50 , withWeight=True)
# for x in tags:
#     print(x)
