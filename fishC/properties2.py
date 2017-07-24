class MyDeceptor:
    #下面三个都是特殊类型
    def __get__(self, instance, owner):
        print('getting....',self, instance, owner)
    def __set__(self, instance, value):
        print('setting...',self, instance)
    def __delete__(self, instance):
        print('delting...', self, instance)


class Test:
    #实现特殊类型的类的实例指派给某个类的属性X ，MyDeceptor即为描述符
    x = MyDeceptor()

test = Test()
test.x = 1
print(test)