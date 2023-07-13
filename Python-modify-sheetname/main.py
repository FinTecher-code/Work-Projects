from cnocr import CnOcr
import os 
import pandas as pd
'''将读取的图片名给excel中各个sheet命名并给出目录页'''

#1.读取图片文件夹路径
path='testPics'

#2.建立空白excel文件“img.xlsx”,a表示追加sheet(追加不覆盖)
writer=pd.ExcelWriter('sheet改名.xlsx')		# pylint: disable=abstract-class-instantiated 

#3.将图片文件夹里的文件名写入新的列表
list=[]             #建立新的列表list
#3.1遍历图片文件夹
for root,dirs,files in os.walk(path):
#os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
# root 表示当前正在访问的文件夹路径
# dirs 表示该文件夹下的子目录名list
# files 表示该文件夹下的文件list

#3.2遍历文件list里的所有的图片文件写入新列表list中
	for file in files:
		file=file.rstrip(".png")          #将图片名末尾的“.png”去掉
		list.append(file)                 #将图片名加入新列表list中        

#4.将列表list嵌套进字典data中
dict_={'filename':list}   #键名为新建表格的字段名，值为以图片名为元素的列表
#5.转换成dataframe格式
df=pd.DataFrame(dict_)
df.to_excel(writer,'目录页',startcol=0,index=False)
df = pd.DataFrame(None)
for i in range(1,len(list)):
    #6.储存在开始建立的excel中
	df.to_excel(writer,list[i],startcol=0,index=False)
#7.保存文件
writer.save()




