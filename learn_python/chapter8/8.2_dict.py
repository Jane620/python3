#-*- coding:utf-8 -*-


'''
D.keys() 键
D.values() 值
D.items() 键值
D.get(k,default) 获取KEY值
D.pop(k) 删除KEY
'''

dict_t = {'name':'john', 'age':'4'}

list_key = [x for x in dict_t.keys()]
list_keys = list(dict_t.keys())
list_Value = [x for x in dict_t.values()]
list_item = [ {x,y} for x,y in dict_t.items()]
print(list_key)
print(list_keys)
print(list_Value)
print(list_item)

values = dict_t.get('age1','10')
if '4' in values:
    print(True)
else:
    print(values)

try:
    # 本版本目前返回为None
    print('value:',dict_t.get('age2'))
except KeyError:
    print('no match')

# fromkeys 创建一个dict
dict_a = dict.fromkeys([1,2,3],0)
print(dict_a)

# zip将列表的行列转换
list_b = list(zip([1,2,3],[4,5,6]))
dict_b = dict(zip([1,2,3,],[4,5,6]))
print(list_b)
print(dict_b)

# 直接赋值
dict_c = dict(a = 1, b =2 ,c =3)
print(dict_c)

