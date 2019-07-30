# @author: huhao
# @file: image_denoising.py
# @time: 2019/7/12 8:19
# @Document：https://www.python.org/doc/
# @desc:


import numpy as np
import scipy as sp

from scipy.fftpack import fft2,ifft2        # ifft2 inverve 反转
import matplotlib.pyplot as plt
# print(sp.__version__)       # 1.3.0


# 登月图片去噪
img = plt.imread('./moon landing.png')
print(img.shape)
# plt.figure(figsize=(12,7))
# plt.imshow(img, cmap=plt.cm.gray)
# plt.show()

# 图片不平滑，存在噪声，波动比较大
# 傅里叶变换：时域-->频域（波动）
# 将波动大的数据过滤掉，在频域中
img_fft = fft2(img)
print(img_fft)

# 计算所有数据波动频率的平均值
print(np.abs(img_fft).mean())       # 51.193375

# 将大于n倍平均值的波动过滤掉
n = 12
cond = np.abs(img_fft) > 100*n
img_fft[cond] = 0
print(img_fft)

# ifft将频域再转换成时域
img_result = ifft2(img_fft)
print(img_result)

# 去除虚数
img2 = sp.real(img_result)

fig = plt.figure(figsize=(12,7))
plt.subplot(1,2,1)
plt.imshow(img, cmap=plt.cm.gray)
plt.subplot(1,2,2)
plt.imshow(img2, cmap=plt.cm.gray)
plt.show()
