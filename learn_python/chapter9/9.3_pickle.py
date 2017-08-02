#-*- coding:utf-8 -*-

import pickle

'''
pickle用于存储python对象到文件
'''

dict_a = dict.fromkeys('ab',0)
dict_file = open(r'..\resource\pickle.pkl','wb')
pickle.dump(dict_a,dict_file)
dict_file.close()

# 读取
read_file = open(r'..\resource\pickle.pkl','rb')
line = pickle.load(read_file)
print(line)
