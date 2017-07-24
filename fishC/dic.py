dict1 = {'a':'1','b':'2','c':'3'}

print('a :',dict1['a'])

dict2 = dict(aa=22,bb=33)
print(dict2)

dict2['aa'] = 44
print(dict2)

dict2['cc'] = 55
print(dict2)


dict3 = {}
dict4 = {}
dict3.fromkeys((1,2,3))
print(dict3)
dict4.fromkeys(1,'aaa')
print(dict4)