b = 'i love fishc com'

b = list(b)

c = (1,1,2,3,5,8,13,21,34)
c= list(c)

a= []
print(max(b))

#list 可以用来直接转换对象为具体内容
a= [1,2,4,576,-10,12.98]
print(reversed(a))
#反转
print(list(reversed(a)))
#列出，并带上index组成元组
print(list(enumerate(a)))

b= [2,3,4,5,6]
#合并
print(list(zip(a,b)))