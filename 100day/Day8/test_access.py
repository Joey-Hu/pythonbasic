# @author: huhao
# @file: test_access.py
# @time: 2019/7/16 16:17
# @Document：https://www.python.org/doc/
# @desc:




# class Test:
#
#     def __init__(self, foo):
#         self.foo = foo
#
#     def __bar(self):
#         print(self.__foo)
#         print("__bar")
#
#
# def main():
#     test = Test('hello')
#     # AttributeError: 'Test' object has no attribute '__bar'
#     test.__bar()
#     # AttributeError: 'Test' object has no attribute '__foo'
#     print(test.__foo)
#
#
# if __name__ == '__main__':
#     main()


class Test:

    def __init__(self, foo):
        self.foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    test = Test('hello')
    # AttributeError: 'Test' object has no attribute '__bar'
    test._Test__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test._Test__foo)


if __name__ == '__main__':
    main()