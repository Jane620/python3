import random as r

class fish:
    def __init__(self,name):
        self.name = name
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print('%s的位置:' %self.name ,self.x,self.y)

class Goldfish(fish):
    pass

class Carp(fish):
    pass

class Salmon(fish):
    pass

class Shark(fish):

    def __init__(self,name):
        super().__init__(name)
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('%s准备进食' %self.name)
            self.hungry = False
        else:
            print('%s吃饱了' %self.name)


salmon1 = fish('Salmon')
salmon1.move()
salmon1.move()
goldfish = fish('goldfish')
goldfish.move()
shark1 = Shark('shark')
shark1.move()
shark1.eat()
shark1.move()
shark1.eat()