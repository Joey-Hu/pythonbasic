# @author: huhao
# @file: Random walk.py
# @time: 2019/7/9 18:31
# @Document：https://www.python.org/doc/
# @desc:

import random
import matplotlib.pyplot as plt
import numpy as np

position = 0
walk = [position]
steps = 1000

for i in range(steps):
    if random.randint(0,2):
        step = 1
    else:
        step = -1

    position += step
    walk.append(position)
walk_nd = np.array(walk)
plt.plot(np.array([0,10,100,1000]), walk_nd)
plt.show()
