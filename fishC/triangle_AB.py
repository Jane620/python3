class Triangle:
    def __init__(self,lenght = 0,width = 0):
        self.lenght = lenght
        self.width = width

    def getLength(self):
        return (self.lenght + self.width) * 2

    def delSquare(self):
        pass

    def __setattr__(self, name, value):
        if name == 'square':
            print('square')
            self.lenght = value
            self.width = value
        else:
            #super().__setattr__(name,value)
            self.__dict__[name] = value


s = Triangle(2,2)
print(s.getLength())
s.square = 5
print(s.width,s.lenght)
s.good = 1
print(s.__dict__)
