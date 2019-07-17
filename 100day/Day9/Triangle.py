# @author: huhao
# @file: Triangle.py
# @time: 2019/7/16 17:34
# @Document：https://www.python.org/doc/
# @desc:

import math


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        if a + b > c and b + c > a and c + a > b:
            return True

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


if __name__ == '__main__':
    # 用字符串的split方法将字符串拆分成一个列表
    # 再通过map函数对列表中的每个字符串进行映射处理成小数
    a, b, c = map(lambda x: (float)(x), input("请输入三条边").split())

    if Triangle.is_valid(a, b, c):
        triangle = Triangle(a, b, c)
        print("周长：" + triangle.perimeter())
        print("面积：" + triangle.area())
    else:
        print("不能组成")
