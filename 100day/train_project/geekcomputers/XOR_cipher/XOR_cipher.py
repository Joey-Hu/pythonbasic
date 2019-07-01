#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: XOR_cipher.py
# @time: 2019/7/1 17:02
# @Ducument：https://www.python.org/doc/
# @desc: 简单异或密码（英语：simple XOR cipher）是密码学中一种简单的加密算法

class XORCipher(object):
    def __init__(self, key = 0):
        """
            simple constructor that receives a key or uses
            default key = 0
        """

        # private field
        self.__key = key

    def encrypt