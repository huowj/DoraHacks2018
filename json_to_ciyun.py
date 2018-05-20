#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 07:19:15 2018

@author: hwj
"""

#coding:utf-8
import re
import sys
import json
import jsonpath
import pandas
from pprint import pprint
from scipy.misc import imread
import jieba    #分词包  
import numpy    #numpy计算包  
import codecs   #codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode   
import pandas    
import matplotlib  
matplotlib.use('TKAgg')  
import matplotlib.pyplot as plt  
from wordcloud import WordCloud#词云包
from wordcloud import WordCloud,ImageColorGenerator

with open('/hwj/dorahacks/gaojin.json','rb') as f:
    x = f.read()
    
result = json.loads(x)

pprint(result[1])


action_list=jsonpath.jsonpath(result,"$..action_text")
action_time_list=jsonpath.jsonpath(result,"$..created_time")
excerpt_list=jsonpath.jsonpath(result,"$..content")


print(len(action_list))
print(len(action_time_list))
print(len(excerpt_list))

excerpt_total=''
for i in range(len(excerpt_list)):
    excerpt_total+=excerpt_list[i]


x=re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\>\:\=\/\!\.\_\?\(\)\-\？\（\）\！\，\：]", "", excerpt_total)
print(x)

content=x

segment=[]  
segs=jieba.cut(content) #切词  
for seg in segs:  
    if len(seg)>1 and seg!='\r\n':  
        segment.append(seg)
        
words_df=pandas.DataFrame({'segment':segment})  
words_df.head()  
stopwords=pandas.read_csv("/hwj/dorahacks/stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'],encoding="utf8")
#去掉我们不需要的高频语气词等  
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]

words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})  
words_stat=words_stat.reset_index().sort_values(by="计数",ascending=False)


bimg=imread('/hwj/dorahacks/1.jpg')  
wordcloud=WordCloud(background_color="black",mask=bimg,font_path='/hwj/dorahacks/STFANGSO.ttf')  
#wordcloud=wordcloud.fit_words(words_stat.head(4000).itertuples(index=False))  
words = words_stat.set_index("segment").to_dict()  
wordcloud=wordcloud.fit_words(words["计数"])  
bimgColors=ImageColorGenerator(bimg)  
plt.axis("off")  
plt.imshow(wordcloud.recolor(color_func=bimgColors))  
plt.show()
print(words_stat[0:9])