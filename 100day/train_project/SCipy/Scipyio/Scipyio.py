# @author: huhao
# @file: Scipyio.py
# @time: 2019/7/12 9:46
# @Document：https://www.python.org/doc/
# @desc:


import  numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from scipy import io

# 随机生成数组，使用scipy中的io.savemat()保存
# 文件格式是mat，标准的二进制文件

# array = np.random.randint(1,100,size=(5,10)).tolist()
# print(array)

list1 = [[74, 92, 14, 38, 70, 73, 99, 12, 57, 47], [53, 6, 46, 77, 82, 74, 89, 41, 86, 74], [4, 94, 85, 94, 89, 55, 38, 41, 54, 96], [8, 61, 9, 54, 43, 71, 8, 83, 11, 49], [39, 40, 50, 98, 82, 7, 72, 10, 8, 49]]

# 保存二进制文件
io.savemat('./list.mat',mdict={'data':list1})


# 加载二进制文件
print(io.loadmat('./list.mat'))
'''
{'__globals__': [], '__version__': '1.0', 'data': array([[74, 92, 14, 38, 70, 73, 99, 12, 57, 47],
       [53,  6, 46, 77, 82, 74, 89, 41, 86, 74],
       [ 4, 94, 85, 94, 89, 55, 38, 41, 54, 96],
       [ 8, 61,  9, 54, 43, 71,  8, 83, 11, 49],
       [39, 40, 50, 98, 82,  7, 72, 10,  8, 49]]), '__header__': b'MATLAB 5.0 MAT-file Platform: nt, Created on: Fri Jul 12 10:12:07 2019'}

'''


