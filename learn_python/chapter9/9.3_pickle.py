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

#二进制处理文件
#>i4sh解释
# > 用于C或者C++中字节对齐
# i -> integer -> 7
# 4s -> 4 strings -> spam
# h -> unsigned short -> 8

bin_file = open(r'..\resource\data.bin','wb')
import struct

data = struct.pack('>i4sh', 17, b'spam', 8)
print(data)
bin_file.write(data)
bin_file.close()

F = open(r'..\resource\data.bin','rb')
data_2 = F.read()
print(data_2)
values = struct.unpack('>i4sh',data_2)
F.close()
print(values)
