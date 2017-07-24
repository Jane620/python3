u'''假设有xyz三个盘，一共有n个木板，从X到Z，则拆解为需要先将n-1个盘借Z移到Y，然后将第n个移动到Z，
    之后换算成需要将n-2个盘借助Z，移动到X，然后将n-1个盘移动到Z...类似斐波那契数列'''

def hannota(n,x,y,z):
    if n ==1:
        print(x,'-->',z)
    else:
        #前一步必定为x到y,x ->y
        hannota(n-1,x,z,y)
        #最后一步肯定是从起点到终点，则必然为x ->z
        print(x,'-->',z)
        #后一步必定为y到z, y->z
        hannota(n-1,y,x,z)

step = int(input("输入汉诺塔的层数:"))

hannota(step,'x','y','z')

