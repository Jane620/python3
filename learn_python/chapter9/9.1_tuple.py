#-*- coding:utf-8 -*-

'''
index 搜索
count 计数
'''


# 创建元组
tuple_a = 1,2
tuple_b = tuple('spamm')

# 方法
try:
    index_a = tuple_a.index(3)
    print(index_a)
except ValueError:
    print('no match')

count_b = tuple_b.count('m')
print(count_b)