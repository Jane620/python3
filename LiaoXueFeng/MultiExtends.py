#-*- coding:utf-8 -*-

__author__ = 'wangjf'

class Flyable:
    def run(self):
        print('fly...')

class Runable:
    def run(self):
        print('run...')

class Bird(Flyable, Runable) :
    pass

if __name__ == '__main__':
    b = Bird()
    # 因此可以推断，当多重继承出现先相同的方法时候，按照继承的顺序优先调用
    b.run()