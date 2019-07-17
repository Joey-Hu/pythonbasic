# @author: huhao
# @file: student.py
# @time: 2019/7/16 15:35
# @Document：https://www.python.org/doc/
# @desc:


def _foo():
    print("test")


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作    --类似于构造函数
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name        # 此处的self类似于java中的this
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s" %(self.name,course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)

    def watch_av(self):
        if self.age < 18:
            print("%s只能观看《熊出没》" % self.name)
        else:
            print("%s正在观看****" % self.name)

def main():
        stu1 = Student("张三", 23)
        stu1.study("python")
        stu1.watch_av()
        stu2 = Student("Joey", 15)
        stu2.study("math")
        stu2.watch_av()

if __name__ == "__main__":
        main()