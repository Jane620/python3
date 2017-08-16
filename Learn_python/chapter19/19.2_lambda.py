#-*- coding:utf-8 -*-

__author__ = 'wangjf'


# 返回函数，其中表达方式为  lambda args : expression
f1 = lambda x : 2 ** x
print(f1(4))

# 此处为不传入参数
f2 = lambda : 3 * 4
print(f2())


import sys

showall = lambda x : list(map(sys.stdout.write,x))
showall2 = lambda x : [sys.stdout.write(line)  for line in x]

t = showall(['this\n','is\n','my\n'])
t2 = showall2(('and\n','so\n','on\n'))

print(t)
print(t2)
