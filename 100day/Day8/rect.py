# @author: huhao
# @file: rect.py
# @time: 2019/7/16 16:35
# @Document：https://www.python.org/doc/
# @desc:


class Rect(object):

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def perimeter(self):
        return (self.__height + self.__width) * 2

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "矩形[%f,%f]" % (self.__width, self.__height)

    def __del__(self):
        # 析构器
        print("销毁矩形对象")


def main():
    rect1 = Rect()
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5,4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())

if __name__ == '__main__':
    main()