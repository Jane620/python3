class Fibs:
    def __init__(self,n =10):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return  self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.n < self.a:
            raise StopIteration
        return self.a


f = Fibs(4)
for each in f:
    print(each)
n=10
while n < 10:
    print(next(f))
    n += 1
