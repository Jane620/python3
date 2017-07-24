class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,x):
        self.num = x

class Pool:
    def __init__(self,x,y):
        #此处实际为实例化的对象，并非为数量
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        #需要返回的是乌龟的数量，即class中定义的num
        print('水池中有乌龟%s只,鱼儿%s条.'%(self.turtle.num,self.fish.num))

p = Pool(1,10)
p.print_num()