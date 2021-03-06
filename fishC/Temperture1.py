class MyProperties:

    def __init__(self,fget=None,fset=None,fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance,value)

    def __delete__(self, instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self,value):
        self._x = value
        print('摄氏度：',self._x)
        print('华氏度：',int(self._x) + 33.8)

    def delX(self):
        del self._x

    x = MyProperties(getX,setX,delX)

c = C()
c.x = 10
print(c.x)