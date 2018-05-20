#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 08:57:38 2018

@author: hwj
"""

from pylab import *
from matplotlib.ticker import  MultipleLocator

from matplotlib.ticker import  FormatStrFormatter

#---------------------------------------------------

 #将x主刻度标签设置为20的倍数(也即以 20为主刻度单位其余可类推)

xmajorLocator = MultipleLocator(5);

#设置x轴标签文本的格式

xmajorFormatter = FormatStrFormatter('%3.1f') 

#将x轴次刻度标签设置为5的倍数
xminorLocator = MultipleLocator() 

#设定y 轴的主刻度间隔及相应的刻度间隔显示格式

#将y轴主刻度标签设置为1.0的倍数
ymajorLocator = MultipleLocator(10.0) 

 #设置y轴标签文本的格式
ymajorFormatter = FormatStrFormatter('%3.1f')

#将此y轴次刻度标签设置为0.2的倍数
yminorLocator = MultipleLocator(10) 

 

#t = arange(1.0, 100.0, 1)
#s=t*exp(-t*1.3)+2*sqrt(t)

 #注意:一般都在ax中设置,不再plot中设置

ax = subplot(111)
plot(year_month_sort,number1,'--r*')

 

#设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

#显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major') #x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度

show()