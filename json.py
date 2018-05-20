#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 16:24:58 2018

@author: hwj

"""
import json
import jsonpath
import pandas
from pprint import pprint

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

import re  
import sys  
import sys  
#sys.setdefaultencoding("utf8")  
  
#def translate(str):  
#    line = str.strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等  
#    p2 = re.compile(ur('[^\u4e00-\u9fa5]')) # 中文的编码范围是：\u4e00到\u9fa5  
#    zh = " ".join(p2.split(line)).strip()  
#    zh = ",".join(zh.split())  
#    outStr = zh  # 经过相关处理后得到中文的文本  
#    return(outStr)
x=re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\>\:\=\/\!\.\_\?\(\)\-\？\（\）\！\，\：]", "", excerpt_total)
print(x)



#print(translate(content_total))


#for i in city_list:  
#    print(i)  
  
#dumps()默认中文伟ascii编码格式，ensure_ascii默认为Ture  
#禁用ascii编码格式，返回Unicode字符串  
#array=json.dumps(city_list,ensure_ascii=False)  
#  
##把结果写入到lagouCity.json文件中  
#with open("lagouCity.json","w") as f:
#    f.write(array.encode("utf-8"))