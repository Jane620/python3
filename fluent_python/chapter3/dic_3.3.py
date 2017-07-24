#-*- coding:UTF-8 -*-

#定义一个字典
dict= {"name":"john","addr":"road 181","phone":"123654654"}

'''字典的映射方法，常用与dict，defaultdict,OrderDict,后两个为dict的变种，源自collections模块'''

# clear() 清除dict的内容
#dict.clear();
print(dict)

# _contains__ 检查key(x)是否在dict中，不能用于检查value
flag= dict.__contains__("name")
print(flag)

# copy()  复制一份dict，为不同对象
dict_cp = dict.copy()
print(dict_cp)
print("dict is {0}:{1}\ndict_cp is {2}:{3}".format(dict,id(dict),dict_cp,id(dict_cp)))

# __delitem__(X)  删除key=X的元素对 即 del dic[x]
dict_cp.__delitem__("name")
print(dict_cp)

# fromkeys(it,[initial]) 将it迭代器中的值重新映射为一个key：value的key，如果有initial，就把他作为这些键的值
print(dict)
dict_fk = {}
#单循环dict，仅获取key
for it in dict:
    x = dict_fk.fromkeys(it,2)
    print("1 {0}:{1}".format(it,x))
print(dict_fk)

# get(k,[default]) 返回k对应的值，没有则返回默认default或者none

name = dict.get("name")
name2 = dict.get("name2","no man")
print("{0}:{1}".format(name,name2))

# d.__getitem__(k) 等同d[k] ,以d[k]的方式，因此需要注意异常

getName = dict.__getitem__("name")
#getName2 = dict.__getitem__("name2")
print("{0}".format(getName))

# item()返回所有的键值对
for key, value in dict.items():
    print("{0}={1}".format(key,value),end=" ")

# __iter__()返回迭代器,即等同dict本身，仅返回key
print()
it = dict.__iter__()
print(list(it))
for key in dict.__iter__():
    print(key)

# keys() 返回所有键
print("keys() 返回所有键")
key_list = dict.keys()
for key in key_list:
    print(key)
#print(key_list)

# __len__() 返回键值对的个数
dict["location"]= 'none'
dic_len = dict.__len__()
print(dic_len)

# __missing__(k) 当__getitem__方法找不到时，调用此方法

# move_to_end

# pop(k,[default]) 返回k对应的值，并删除这个节点，找不到则返回none
print("pop(k,[default]) 返回k对应的值，并删除这个节点，找不到则返回none")
name = dict.copy().pop("name")
name2 = dict.copy().pop("name2","no man 2")
print("{0}:{1}".format(name,name2))

# popitem()随机返回一个值，并删除键值对
print("popitem()随机返回一个值，并删除键值对")
dict_random = dict.copy()
random_value = dict.copy().popitem()
print(random_value)
print(dict_random)

# __reversed__() 反转

