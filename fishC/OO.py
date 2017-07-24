
class Person:
    name = "测试名"


p = Person()
print(p.name)

class Person1:
    #private args
    __name = '测试名2'

    def getName(self):
        return self.__name

p = Person1()
#print(p.__name)
print(p._Person1__name)
print(p.getName())