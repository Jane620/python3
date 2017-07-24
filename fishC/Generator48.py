def myGen():
    print('生成器执行...')
    yield  1
    yield  2

myG = myGen()
print(next(myG))
print(next(myG))
#print(next(myG))
print('--------------')
for i in myGen():
    print(i)

def fibs():
    a = 0
    b = 1
    while True:
        a ,b = b ,a+b
        yield a

for each in fibs():
    if each > 100:
        break
    print(each,end=' ')

print('--------------')
#能被2整除，因此not为正，且不能被3整除
i = [i for i in range(100) if not(i%2) and (i%3)]
print(i)