
class Parent():
    def hello1(self):
        print('调用父类函数....')

class Child(Parent):
    pass

p = Parent()
p.hello1()
p1 = Child()
p1.hello1()