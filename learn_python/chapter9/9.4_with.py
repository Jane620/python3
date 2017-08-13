#-*- coding:utf-8 -*-

# with open() as xx
with open(r'..\resource\textfile','rb') as f:
    for line in f.readlines():
        print(line)


t = (4,5,6)
t_2 = (1,)+t[1:]
print(t_2)

t_3 = list(t)
t_3[0] =  1
print(tuple(t_3))
