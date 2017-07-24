#-*- coding:utf-8 -*-

# why?
L = [1,2]
L.append(L)
print(L)

# 二维数组，其中首位为行，第二个为列
M = [[1,2,3],[4,5,6],[7,8,9]]
print(M[1])
print(M[1][2])

#row为每一行，因此如果单取每行的第二列则，直接用row[1]
col2 = [row[1] for row in M]
print(col2)
