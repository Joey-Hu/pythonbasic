#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: XOR_cipher.py
# @time: 2019/7/1 17:02
# @Ducument：https://www.python.org/doc/
# @desc: 简单异或密码（英语：simple XOR cipher）是密码学中一种简单的加密算法，异或运算a⊕b = (¬a ∧ b) ∨ (a ∧¬b) 相同为0，不同为1

"""
	author: Christian Bender
	date: 21.12.2017
	class: XORCipher

	This class implements the XOR-cipher algorithm and provides
	some useful methods for encrypting and decrypting strings and
	files.

	Overview about methods

	- encrypt : list of char
	- decrypt : list of char
	- encrypt_string : str
	- decrypt_string : str
	- encrypt_file : boolean
	- decrypt_file : boolean
"""


class XORCipher(object):

    def __init__(self, key=0):
        """
            simple constructor that receives a key or uses
            default key = 0
        """

        # private field
        self.__key = key

    def encrypt(self, content, key):
        """
            input: 'content' of type string and 'key' of type int
            output: encrypted string 'content' as a list of chars
            if key not passed the method uses the key by the constructor.
            otherwise key = 1
        """

        # precondition
        assert (isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        # make sure key can be any size
        # 二进制减法：a-b = a + (-b)
        # b -> (-b): 各位（包括符号位）取反加1
        while (key > 255):
            key -= 255

        # This will be returned
        ans = []

        for ch in content:
            ans.append(chr(ord(ch) ^ key))      #将每个字符与key进行异或操作并写入ans[]中

        return ans

    def decrypt(self, content, key):
        """
            input: 'content' of type list and 'key' of type int
            output: decrypted string 'content' as a list of chars
            if key not passed the method uses the key by the constructor.
            otherwise key = 1

            解码原理：对字符再次与key进行异或运算
        """

        # precondition
        assert (isinstance(key, int) and isinstance(content, list))
        # 注意这边的content已经经过加密之后变成了list类型

        key = key or self.__key or 1

        # make sure key can be any size
        while (key > 255):
            key -= 255

        # This will be returned
        ans = []

        for ch in content:
            ans.append(chr(ord(ch) ^ key))

        return ans

    def encrypt_string(self, content, key=0):
        """
            input: 'content' of type string and 'key' of type int
            output: encrypted string 'content'
            if key not passed the method uses the key by the constructor.
            otherwise key = 1
        """

        # precondition
        assert (isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        # make sure key can be any size
        while (key > 255):
            key -= 255

        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def decrypt_string(self, content, key=0):
        """
            input: 'content' of type string and 'key' of type int
            output: decrypted string 'content'
            if key not passed the method uses the key by the constructor.
            otherwise key = 1
        """

        # precondition
        assert (isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        # make sure key can be any size
        while (key > 255):
            key -= 255

        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def encrypt_file(self, file, key=0):
        """
            input: filename (str) and a key (int)
            output: returns true if encrypt process was
            successful otherwise false
            if key not passed the method uses the key by the constructor.
            otherwise key = 1
        """

        # precondition
        assert (isinstance(file, str) and isinstance(key, int))

        try:
            with open(file, "r") as fin:
                with open("encrypt.out", "w+") as fout:     # 新建输出结果文件
                    # actual encrypt-process
                    for line in fin:
                        fout.write(self.encrypt_string(line, key))

        except:
            return False

        return True

    def decrypt_file(self, file, key):
        """
            input: filename (str) and a key (int)
            output: returns true if decrypt process was
            successful otherwise false
            if key not passed the method uses the key by the constructor.
            otherwise key = 1
        """

        # precondition
        assert (isinstance(file, str) and isinstance(key, int))

        try:
            with open(file, "r") as fin:
                with open("decrypt.out", "w+") as fout:
                    # actual encrypt-process
                    for line in fin:
                        fout.write(self.decrypt_string(line, key))

        except:
            return False

        return True


# Tests
crypt = XORCipher()
key = 67

# # test enrcypt
print(crypt.encrypt("hallo welt",key))
# print(crypt.encrypt(123,key))
'''
Traceback (most recent call last):
  File "D:/Desktop/python/python_basics/100day/train_project/geekcomputers/XOR_cipher/XOR_cipher.py", line 196, in <module>
    print(crypt.encrypt(123,key))
  File "D:/Desktop/python/python_basics/100day/train_project/geekcomputers/XOR_cipher/XOR_cipher.py", line 51, in encrypt
    assert (isinstance(key, int) and isinstance(content, str))
AssertionError
'''
# # test decrypt
print(crypt.decrypt(crypt.encrypt("hallo welt",key), key))

# # test encrypt_string
print(crypt.encrypt_string("hallo welt",key))

# # test decrypt_string
print(crypt.decrypt_string(crypt.encrypt_string("hallo welt",key),key))

if (crypt.encrypt_file("test.txt",key)):
	print("encrypt successful")
else:
	print("encrypt unsuccessful")

if (crypt.decrypt_file("encrypt.out",key)):
	print("decrypt successful")
else:
	print("decrypt unsuccessful")
