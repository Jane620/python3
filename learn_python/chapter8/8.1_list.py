#-*- coding:utf-8 -*-

L = ['aBd', 'ABC', 'abe']
print(id(L))
sorted(L, key=str.lower, reverse=True)
print(L)
print(id(L))

sorted([x.lower() for x in L], reverse=True)
print(L)

# 在原list对象上进行反转
L.reverse()
print(L)
print(id(L))

# 删除特定的几个位置的元素
L[1:2] = []
print(L)