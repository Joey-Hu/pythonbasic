# @author: huhao
# @file: mat_2.py
# @time: 2019/7/16 8:22
# @Document：https://www.python.org/doc/
# @desc:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,50)

fig1 = plt.figure(figsize=(12,7))

# color属性指向线条颜色,可以有以下形式：
plt.subplot(221)
plt.plot(x, np.sin(x), color = "red")     # 英语单词
# plt.plot(x, np.sin(x), color = "#ffff00") # 十六进制
# plt.plot(x, np.sin(x), color = (0.3,0.3,0.4))   # 数字

# 透明度设置
plt.subplot(222)
plt.plot(x, np.sin(x), color = "red", alpha = 0.5)

# 背景颜色
plt.subplot(223,facecolor = "yellow")       #
plt.plot(x, np.sin(x), color = "red")

# linestyle和线宽
plt.subplot(224)
# plt.plot(x, np.sin(x), linestyle = "-")     # 实线
plt.plot(x, np.sin(x), linestyle = "--", lw = 4)      #  破折线和线宽
# plt.plot(x, np.sin(x), linestyle = "-.")       # 点划线
# plt.plot(x, np.sin(x), linestyle = ":")     # 虚线
# plt.plot(x, np.sin(x), linestyle = "steps")     # 阶梯线

# 设置不同宽度的破折线
fig2 = plt.figure(figsize=(12,7))
plt.subplot(221)
plt.plot(x, np.sin(x),dashes = [1,2,5,3,1,2])   # dashes=[线宽，间距，线宽，间距。。。]

# 点型 marker
plt.subplot(222)
# plt.plot(x, np.sin(x), marker = "1")    # 一角朝下的三脚架
# plt.plot(x, np.sin(x), marker = "2", markersize = 15)    # 一角朝上的三脚架
# plt.plot(x, np.sin(x), marker = "3")    # 一角朝左的三脚架
# plt.plot(x, np.sin(x), marker = "4")    # 一角右的三脚架

plt.plot(x, np.sin(x), marker = "s")    # 正方形
'''
s->正方形
h->六边形
8->八边形
p->五边形
H->六边形2
'o'->圆圈
'd'->小菱形
'D'-> 大菱形
'''

plt.subplot(223)
plt.plot(x, np.sin(x), color = "red", marker = "o", markerfacecolor = "y", markeredgecolor = 'b')

plt.show()



x2 = np.linspace(0, 2*np.pi, num=20)
plt.figure(figsize=(12,7))

# 在一条语句中为多个曲线进行设置
# 多个曲线同一设置
plt.subplot(221)
plt.plot(x, np.sin(x), x, np.cos(x), color = "red")

# 多个曲线不同设置
plt.subplot(222)
plt.plot(x, np.sin(x),'r--o', x, np.cos(x), "g:*")  # 无需声明属性名称

# 参数传递
# 对实例使用一系列setter方法
plt.subplot(223)
line1,line2 = plt.plot(x, np.sin(x), x, np.cos(x))
line1.set_color('#FF0000')
line1.set_ls("--")
line2.set_color("g")
line2.set_marker("o")

# x,y刻度
plt.subplot(224)
plt.plot(x,np.sin(x))
plt.xticks(np.arange(0,2*np.pi + 0.01, np.pi/2),[0, "$\pi/2$", "$3\pi/2$", "$2\pi$"])
plt.yticks([-1,0,1],["min",0,"max"], color = "r", fontsize = 20, rotation = 60)
plt.show()






