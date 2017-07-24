#-*- coding:utf-8 -*-

import  random

# random 返回一个[0,1)的实数
num = random.random()
list_num = [1,2,3,4]
#随机选择器
choice = random.choice(list_num)
print("{0}:{1}".format(num,choice))

#find将返回找到该字符串的偏移量，没有则返回-1
test_str = 'this is my way.'
find = test_str.find('is')
find_no = test_str.find('zz')
print(find,find_no)

#replace将找到的字符串进行替换，该方法为全局
replace_str = test_str.replace('is','are')
print(replace_str)

#split根据给定的规则进行分割
split_str = test_str.split('i')
print(split_str)

#大写以及判断字符串
#upper() isalpha必须为全部字母，例如中间有空格，也就不能算作全字符,可以用strip()，衍生的有lstrip,rstrip
upper_Str = test_str.upper()
test_str2 = ' ss '
is_str=test_str2.strip().isalpha()
print(upper_Str,is_str)

#help方法用于直接查询不知道的函数
help(test_str2.strip)

#返回ascii码
print(ord('A'))



