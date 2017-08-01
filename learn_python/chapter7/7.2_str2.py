#-*- coding:utf-8 -*-

# dict 格式化字符串
reply  = '''my name is %(name)s, i'm %(age)d years old.'''
values = {'name':'john','age':4}
print(reply % values)

# vars()返回包含本函数或文件中定义的变量
name = 'kate'
age = 4
print(vars())

if 'name' in vars():
    print(True)

# format 特殊用法
args = list('spam')
print('first={0},last={1}'.format(args[0],args[-1]))
