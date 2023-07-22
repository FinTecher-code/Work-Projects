import pdfplumber  
import jieba
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

with pdfplumber.open('/Users/jiaoxubin/Desktop/Paper.pdf') as f:
    # 用for循环读取文件中的每一页
    for page in f.pages:
        text = page.extract_text()
        txt_f = open(r'Paper.txt',mode='a',encoding='utf-8')
        txt_f.write(text)

file = open('Paper.txt',encoding='utf-8')
file = file.read()
txtlist = jieba.lcut(file)
string = " ".join(txtlist)
stop_words = {}
counts = {}
for txt in txtlist: # 下面将词语去重了，奇怪
    if len(txt) == 1:
        stop_words[txt] = stop_words.get(txt,0) + 1
    else:
        counts[txt] = stop_words.get(txt, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
y1 = []
labels = []
for i in range(1,10):
    y1.append(items[i][1])
    labels.append(items[i][0])

# 热词统计分析
width = 0.3
x = np.arange(len(y1))
a = [i for i in range(0,9)]
plt.xticks(a,labels,rotation=30) 
plt.bar(x = x,height=y1,width=width)
plt.title('pdf文件热词统计分析')
plt.savefig('热词统计分析.png')
plt.show()

# 热词词云生成