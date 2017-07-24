#定义一个不可变列表，每次访问列表中的某个元素后，则对改元素计数
class ListC:
    def __init__(self,*args):
        self.values = [x for x in args]
        #需要优化为value:count的组合，目前其实为一个序列
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return  self.values[item]

C1 = ListC(1,3,5,7,9)
C2 = ListC(2,4,6,8,0)
print(C1[1])
print(C2[1])
print(C1[1]+C2[1])
print(C1.count)


