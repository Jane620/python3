import  math
#没有含义，只是占位
def someday():
    pass


def my_abs(n):
    if not isinstance(n,(int,float)):
        raise TypeError("wrong type")
    if n >= 0:
        return n
    else:
        return -n

#print(my_abs('a'))

def quardratic(a,b,c):
    if a == 0 :
        print('此方程唯一解为 x=%.1f' %(-c/b))
    else:
        flag = (b ** 2) - (4*a*c)
        if flag > 0 :
            x = (-b + math.sqrt(flag))/ (2*a)
            y = (-b - math.sqrt(flag))/ (2*a)
            print('此方程解为：x = %.1f,y = %.1f' %(x,y))
        elif flag == 0:
            x = -b / (2 * a)
            print('此方程具有唯一解：%.1f' % x)
        else:
            print('无解')

quardratic(1,2,3)
quardratic(2,3,1)
quardratic(0,2,3)
quardratic(1,2,1)