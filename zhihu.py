#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 14:33:42 2018

@author: hwj
"""

import jieba
import jieba.analyse as analyse
from wordcloud import WordCloud
import os
from os import path
import matplotlib.pyplot as plt
from scipy.misc import imread



seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))


comment_text=excerpt_total
cut_text=" ".join(jieba.cut(x))
result=jieba.analyse.textrank(cut_text,topK=1000,withWeight=True)
keywords=dict()

for i in result:
    keywords[i[0]] = i[1]
 
d = path.dirname(__file__) # 当前文件文件夹所在目录
color_mask = imread("/hwj/dorahacks/1.jpg") # 读取背景图片
cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        font_path="/hwj/dorahacks/STFANGSO.ttf",
        # font_path=path.join(d,'simsun.ttc'),
        width=200,
        height=200,
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=2000,
        #最大号字体
        max_font_size=40
        )
word_cloud = cloud.generate(cut_text)# 产生词云
word_cloud.to_file("/hwj/dorahacks/user_img.jpg") #保存图片
        #  显示词云图片
plt.imshow(word_cloud)
plt.axis('off')
plt.show()

comment_text = x
# 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云  
cut_text = " ".join(jieba.cut(x))  
print(cut_text)  
# 读取背景图片  
color_mask = imread("/hwj/dorahacks/1.jpg")  
cloud = WordCloud(  
    # 设置背景色  
    background_color='black',  
    # 词云形状  
    mask=color_mask,     
    #允许最大词汇     
    max_words=2000,  
    # 设置字体，不设置可能出现乱码  
    font_path="/hwj/dorahacks/STFANGSO.ttf",  
    #最大号字体  
    max_font_size=100,  
)  
# 产生词云  
word_cloud = cloud.generate(cut_text)  
# 保存图片  
word_cloud.to_file('after.jpg')  
# 显示词云图片  
plt.imshow(word_cloud)  
plt.show()

