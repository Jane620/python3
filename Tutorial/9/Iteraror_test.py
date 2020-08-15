# iterator
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]

R1 = Reverse('ask me why')
result1 = ''
for i in R1:
    result1 = result1 + ''.join(i)
print(result1)

# generator
def reverse(data):
    # range(x, -1, -1) follow X -> 0 ,one by one
    for index in range(len(data)-1 , -1, -1):
        print(f'index is {index}')
        yield data[index]

result2 = ''
for x in reverse('baby'):
    result2 = result2 + ''.join(x)
print(result2)

