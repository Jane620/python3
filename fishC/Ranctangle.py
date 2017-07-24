class Ranctangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getPeri(self):
        return (self.x+self.y)*2
    def getSize(self):
        return self.x * self.y


r = Ranctangle(2,3)
print(r.getPeri())
print(r.getSize())