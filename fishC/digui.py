
u'''f(x)=1*2*3*4*..*n'''

def digui(n):
    # n is a num\
    result = n
    for i in range(1,n):
        result *=i
    return result

def digui2(n):
    result = 0
    if  n ==1:
        result = 1
    else:
        result += n * digui2(n-1)
    return result

def fab1(n):
    a,b=0,1
    if n == 1 or n == 2:
        return 1
    else:
        return fab1(n-1) + fab1(n-2)

a = digui(3)
b = digui2(4)
c = fab1(35)
#print(a)
print(b)
#print(c)