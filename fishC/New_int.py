
class New_int(int):

    def __add__(self, other):
        return int.__sub__(self,other)

    def __sub__(self, other):
        return  int.__add__(self,other)

p1 = New_int(3)
p2 = New_int(4)
#一切皆为对象，其实p1和p2是两个int的对象
#等同 p1 = int('3')
#p2 = iny('4')
print(p1+p2)
print(p1-p2)