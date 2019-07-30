# @author: huhao
# @file: Integral.py
# @time: 2019/7/12 9:28
# @Document：https://www.python.org/doc/
# @desc:

import numpy as np
import scipy as sp

from scipy.fftpack import fft2,ifft2        # ifft2 inverve 反转
from scipy import integrate
import matplotlib.pyplot as plt

# 数值积分，求解圆周率
# 画一个圆
c = lambda x: (1-x**2)**0.5

x = np.linspace(-1,1,100)
y = c(x)

plt.figure(figsize=(5,5))
plt.plot(x,y)
plt.plot(x,-y)
plt.show()


# 求圆的面积
# 使用scipy.integrate进行积分，调用quad()方法
print(integrate.quad(c,-1,1))        # 定积分
'''
(, 1.0002354500215915e-09)
'''
print(1.5707963267948983*2)     # 3.1415926535897967








