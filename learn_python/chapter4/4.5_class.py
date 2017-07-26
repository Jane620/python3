#-*- coding:utf-8 -*-

#定义一个借呗用户
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        #按照空格进行切割，返回最后一位
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay  *= (1 + percent)


john = Worker('john smith',600)
kate = Worker('cary kate',300)
print(john.lastName())
john.giveRaise(.2)
print(john.pay)

list1 = [1,2,3,4]
set1 = set(list1)
set1[1] = 33
print(set1)

