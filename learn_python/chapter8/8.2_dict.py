#-*- coding:utf-8 -*-


'''
D.keys() 键
D.values() 值
D.items() 键值
D.get(k,default) 获取KEY值
D.pop(k) 删除KEY
'''

dict = {'name':'john', 'age':'4'}

list_key = [x for x in dict.keys()]
list_keys = list(dict.keys())
list_Value = [x for x in dict.values()]
list_item = [ {x,y} for x,y in dict.items()]
print(list_key)
print(list_keys)
print(list_Value)
print(list_item)

values = dict.get('age1','10')
if '4' in values:
    print(True)
else:
    print(values)