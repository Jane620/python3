#-*- coding:utf-8 -*-

__author__ = 'wangjf'

class MainOperator:

    def __init__(self,a):
        self.a = a

    def __add__(self,other):
        print(self.a - other)


class TestOperator(MainOperator):

    def __init__(self,value):
        self.data = value
        print(self.data)

    def __add__(self, other):
        return TestOperator(self.data + other)

if __name__ == '__main__':
    data = TestOperator(6)
    b = data + 6