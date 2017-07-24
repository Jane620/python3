#将内容转换成二进制内容
import pickle as p

my_list = ['1','2','3','王大毛']

#以二进制方式写入
pickle_file = open('resource/mylist.pkl','wb')
p.dump(my_list,pickle_file)
pickle_file.close()

#二进制方式读取
read_file = open('resource/mylist.pkl','rb')
list = p.load(read_file)
print(list)