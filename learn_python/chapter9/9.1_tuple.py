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

# 元祖不可改变 ，排序通过list进行中转
tuple_2 = 1,3
tuple_3= tuple_2 + (2,4)
print(tuple_3)

tmp = list(tuple_3)
tmp.sort()
tuple_3 = tuple(tmp)

print(tuple_3)

#元祖内部的可变内容是可以修改的
tuple_4 = (1,['aaa'],2)
tuple_4[1][0] = 'bbb'
print(tuple_4)