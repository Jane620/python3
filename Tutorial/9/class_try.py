
class Duck:
    common = ['swim', 'fly', 'sound']

    def __init__(self, name):
        self.properties = []
        self._add(name, self.common)

    def add(self, name, skill):
        for i in skill:
            if name == "black":
                self.properties.append(i)
            elif name == 'white':
                self.properties.append('swim')
            else:
                self.properties.append('fly')
    _add = add

D1 = Duck('black')
D2 = Duck('white')
D3 = Duck('blue')
print(D1.properties)
print(D2.properties)
print(D3.properties)
