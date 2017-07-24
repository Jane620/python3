#过滤奇数
# n ==0 || n // 2 ! ==0

def filterj(n):
        return n %2

a = lambda n:n%2
temp = range(10)
result = filter(a,temp)
print(list(result))
