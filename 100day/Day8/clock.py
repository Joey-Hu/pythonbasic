# @author: huhao
# @file: claock.py
# @time: 2019/7/16 16:47
# @Document：https://www.python.org/doc/
# @desc:

import os
import time

class Clock(object):

    # 初始化
    def __init__(self, hour=0, minute=0, second=0):     # 初始化是不给h, m, s赋值时，默认值=0
        self._hour = hour
        self._minute = minute
        self._second = second

    # 运行
    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    # 显示时间
    def show(self):
        return "%02d:%02d:%02d" %(self._hour, self._minute, self._second)

if __name__ == '__main__':
    clock = Clock(23,59,55)
    # for i in range(10):
    #     clock.run()
    #     print(clock.show())
    # print(clock.show())
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()
