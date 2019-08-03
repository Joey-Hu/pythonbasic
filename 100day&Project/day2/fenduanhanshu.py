#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: fenduanhanshu.py
# @time: 2019/5/9 16:04
# @Ducument：https://www.python.org/doc/
# @desc: 分段函数求值
'''

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

'''

x = float(input("输入x:"))

if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print("x = %.2f, y = %.2f" %(x, y))

'''
当然根据实际开发的需要，分支结构是可以嵌套的，例如判断是否通关以后还要根据你获得的宝物或者道具的数量对你的表现给出等级（比如点亮两颗或三颗星星），那么我们就需要在if的内部构造出一个新的分支结构，同理elif和else中也可以再构造新的分支，我们称之为嵌套的分支结构，也就是说上面的代码也可以写成下面的样子。

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))


**说明：**大家可以自己感受一下这两种写法到底是哪一种更好。在之前我们提到的Python之禅中有这么一句话“Flat is better than nested.”，之所以提出这个观点是因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，如果可以使用扁平化的结构就不要去用嵌套，因此之前的写法是更好的做法。
'''