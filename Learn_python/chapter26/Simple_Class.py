#-*- coding:utf-8 -*-

__author__ = 'wangjf'


class rec : pass


if __name__ == '__main__':
    rec.name = 'jane'
    rec.age = '30'
    x = rec()
    y = rec()
    print(x.name,y.name)
    x.name = 'jessica'
    print(rec.name,x.name)
    print(rec.__dict__.keys())
    # 表明x的类属性由自身定义，其他源自继承
    print(x.__dict__.keys())
    # 表明y的所有类属性源自继承
    print(y.__dict__.keys())