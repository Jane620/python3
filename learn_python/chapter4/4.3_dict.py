#-*- coding:utf-8 -*-

# while循环用法，递减打印
count = 5
while count > 0:
    print("1 "*count)
    count -=1

# list解析
list_origin = [1,2,3,4,5]
list_sum = [x * 2 for x in list_origin]
print(list_sum)
print('--------')
def double_Num(x):
    return x * 2
list_sum2 = map(double_Num , list_origin)
print(list(list_sum2))

#判断字典中key是否存在
dict_origin = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
dict_origin['e'] = 5
print(dict_origin)
#dict_origin['f'] 找不到键异常，keyerror，可以采用其他方式
flag =  'f' in dict_origin
print(flag)

#方法2 ， 采用get ，可以给不存在的赋予一个默认值  等价于一个if判断
value = dict_origin.get('f',None)
value2 = dict_origin['f'] if 'f' in dict_origin else None
print(value)
print(value2)
