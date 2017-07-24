classmate = ['john','cate','gray']
print(classmate)
print(len(classmate))
print(classmate[0])
print(classmate[1:])
#末尾增加和特定位置增加
classmate.append('bob')
print(classmate)
classmate.insert(1,'green')
print(classmate)
#末尾删除或特定位置删除
classmate.pop()
print(classmate)
classmate.pop(1)
print(classmate)
#替换某个值
classmate[0] = 'Jorse'
print(classmate)
#列表中的列表
classmate.append(['big','small'])
print(classmate)
print(classmate[-1][0])