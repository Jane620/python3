class D:
    def __getattribute__(self, item):
        print('getattribute')
        return super().__getattribute__(item)
    def __getattr__(self, item):
        print('getattr')
    def __setattr__(self, key, value):
        print('setattr')
        super().__setattr__(key,value)
    def __delattr__(self, item):
        print('delattr')
        super().__delattr__(item)

d = D()
print('---------first')
d.x
print('---------second')
d.x =1
print('---------third')
d.x