# @author: huhao
# @file: XOR_cipher_1.py
# @time: 2019/7/8 18:21
# @Document：https://www.python.org/doc/
# @desc:


class XORCipher(object):
    def __init__(self, key=0):
        self.__key = key

    def encrypt(self,content, key):
        assert (isinstance(key, int) and isinstance(content,str))

        key = key or self.__key or 1

        while(key>255):
            key -= 255

        ans = []

        for ch in content:
            ans.append(chr(ord(ch) ^ key))

        return ans


    def decrypt(self, content,key):
        assert (isinstance(key, int) and isinstance(content, list))

        key = key or self.__key or 1

        while (key > 255):
            key -= 255

        ans = []

        for ch in content:
            ans.append(chr(ord(ch) ^ key))

        return ans

    def encrypt_string(self, content, key):
        assert (isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        while (key > 255):
            key -= 255

        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def decrypt_string(self, content, key):
        assert (isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        while (key > 255):
            key -= 255

        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def encrypt_file(self, file, key):
        assert (isinstance(key, int) and isinstance(file, str))

        try:
            with open(file, "r") as fin:
                with open("encrypt.out", "w+") as finout:
                    for line in fin:
                        finout.write(self.encrypt_string(line, key))

        except:
            return False

        return True

    def decrypt_file(self, file, key):
        assert (isinstance(key, int) and isinstance(file, str))

        try:
            with open(file, "r") as fin:
                with open("decrypt.out", "w+") as finout:
                    for line in fin:
                        finout.write(self.decrypt_string(line, key))

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

# if (crypt.encrypt_file("test.txt",key)):
# 	print("encrypt successful")
# else:
# 	print("encrypt unsuccessful")
#
# if (crypt.decrypt_file("encrypt.out",key)):
# 	print("decrypt successful")
# else:
# 	print("decrypt unsuccessful")
