#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 19:42:17 2018

@author: hwj
"""


import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#timeArray=time.localtime(action_time_list)
#otherStyleTime=time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
#print(otherStyleTime[9])

timeArray=[0]*len(action_time_list)
otherStyleTime=[0]*len(action_time_list)
year=[]
month=[]
day=[]
hour=[]
minute=[]
second=[]
year_month=[]
for i in range(len(action_time_list)):
    timeArray[i]=time.localtime(action_time_list[i])
    otherStyleTime[i]=time.strftime("%Y--%m--%d %H:%M:%S", timeArray[i])
    year.append(timeArray[i][0])
    month.append(timeArray[i][1])
    day.append(timeArray[i][2])
    hour.append(timeArray[i][3])
    minute.append(timeArray[i][4])
    second.append(timeArray[i][5])
    year_month.append(time.strftime("%Y-%m", timeArray[i]))
    
print(year_month[9])
    
#print(timeArray[9],otherStyleTime[9])
#print(list(set(hour)))

number=[]
for i in list(set(hour)):
    number.append(hour.count(i))

#标签
labels = np.array((list(set(hour))))
#数据个数
dataLenth = 24
#数据
data = np.array(number)


angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) 
angles = np.concatenate((angles, [angles[0]])) 
 
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'ro-', linewidth=2)
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
ax.set_title("gaojin_action_radar", va='bottom', fontproperties="SimHei")
ax.grid(True)
plt.show()

a=pd.DataFrame(list(zip(labels,number)),columns=['labels','numbers'])
print(a)

from matplotlib.dates import AutoDateLocator, DateFormatter  
autodates = AutoDateLocator()  
#yearsFmt = DateFormatter('%Y-%m-%d %H:%M:%S')  



year_month_sort=sorted(list(set(year_month)))
number1=[]
for j in list(set(year_month_sort)):
    number1.append(year_month.count(j))
    
plt.figure(1)
plt.plot(year_month_sort,number1)