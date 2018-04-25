#-*- coding:utf-8 -*-

__author__ = 'wangjf'

class Animal:

    def __init__(self,name,size):
        self._name = name
        self._size = size

    def say(self):
        return "name:" + self._name + ",size:" + self._size


class Dog(Animal):

    def hi(self):
        print(self.say())

class Cat(Animal):

    def hi(self):
        print(self.say())

if __name__ == '__main__':
    dog = Dog('jb','20')
    cat = Cat('dw','10')
    dog.hi()
    cat.hi()

