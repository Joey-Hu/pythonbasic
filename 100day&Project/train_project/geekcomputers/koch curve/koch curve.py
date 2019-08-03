#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: koch curve.py
# @time: 2019/6/28 15:04
# @Ducument：https://www.python.org/doc/
# @desc:


from turtle import *

def snowflake(lengthSide,levels):
    if levels == 0:
        forward(lengthSide)     #向右绘制
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)
    right(120)
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)

if __name__ == '__main__':
    speed(0)    #defining the speed of the turtle
    length = 300.0
    penup()  # Pull the pen up – no drawing when moving.

    backward(length / 2.0)
    pendown()
    for i in range(3):
        # Pull the pen down – drawing when moving.
        snowflake(length, 2)
        right(120)
        # To control the closing windows of the turtle
    mainloop()