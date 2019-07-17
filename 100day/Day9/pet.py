# @author: huhao
# @file: pet.py
# @time: 2019/7/17 11:27
# @Document：https://www.python.org/doc/
# @desc:


from abc import ABCMeta, abstractmethod


class pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(pet):
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(pet):
    def make_voice(self):
        print('%s: 喵..喵..喵...' % self._nickname)

if __name__ == '__main__':
    pets = [Dog("旺财"), Cat("凯迪"), Dog("大黄")]
    for pet in pets:
        pet.make_voice()