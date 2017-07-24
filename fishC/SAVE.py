#持久化
#简单方式采用文件形式保存

f = open('aa.txt')
#print(f)
print(f.read(6))
print(f.tell())#返回位置
print(f.seek(3,0))

#f.close()
#for i in f.readline():
#    print(i)
f.seek(0,0)
for each in f:
    print(each)

if f.writable():
    print('1')
else:
    print('0')

#覆盖写
f2 = open('aa.txt','w')
f2.write('i love this one')
f.close()


for i in f2:
    print(i)