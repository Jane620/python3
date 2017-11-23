#-*- coding:utf-8 -*-

__author__ = 'wangjf'

''''
有经验的OOP程序员一般会先建一个超类
拥有通用行为,，因此可以针对不同的员工编写不同的特性

'''
class Employee:

    def __init__(self,name):
        self.name = name

    def computerSallary(self):
        pass
    def giveRaise(self):
        pass
    def promote(self):
        pass
    def retire(self):
        pass

class Counter(Employee):

    def __init__(self):
        super()

    def giveRaise(self):
        pass

class Engineer(Employee):
    def giveRaise(self):
        pass

bob = Counter()
john = Engineer('name')
