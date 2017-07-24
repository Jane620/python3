a = {1:'one',2:'two',3:'three'}
b = a.copy()
c = a

#检查地址
print(id(a))
print(id(b))
print(id(c))

c[4] = 'four'
print(a)
print(b)
print(c)