#-*- coding:utf-8 -*-


#读取配置文件，并将文件的配置改造成key:value 或者 key = value的形式

def readfile(filename):
    dict = {}
    with open(filename,'r') as fp:
        for line in fp.readlines():
            key = line.strip('\n').split('=')[0]
            value = line.strip('\n').split('=')[1]
            dict[key] = value
    return dict

dict = {'a':'1','b':'2'}
dict.pop('a')
print(dict)