import os

#获取工作目录
print(os.getcwd())
#改变工作目录
print(os.chdir('D:\\'))
#列出所有文件
print(os.listdir('D:\\'))
#创建单层目录
#os.mkdir('D:\\A')
#创建多层目录
#os.makedirs('D:\\A\\B')
#删除文件，目录和递归删 remove rmdir removedirs
#重命名 rename(old,new)
#执行系统命令 system(command)
#os.system('cmd')
#当前和上一级目录
print(os.curdir)
print(os.pardir)
print(os.listdir(os.curdir))

import os.path
#去掉目录路径返回的文件名,以及返回文件路径
print(os.path.basename('D:\\ASF\\ASF.exe'))
print(os.path.dirname('D:\\ASF\\ASF.exe'))
#组合路径
print(os.path.join('D:\\','A','B'))
#分割文件名和路径
print(os.path.splitext('D:\ASF\ASF.exe'))