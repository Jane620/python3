def hannoi(n,x,y,z):
    if n == 1:
        print(x,'-->',z)
    else:
        # 分三步，将n-1个盘从x移动到y,将最底下那个n从x移动到z，之后将n-1个从y移动到z
        hannoi(n-1,x,z,y)
        print(x,'-->',z)
        hannoi(n-1,y,x,z)

while True:
    step = int(input("输入汉诺塔层数："))
    hannoi(step,'x','y','z')
