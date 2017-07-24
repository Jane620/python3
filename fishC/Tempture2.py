class Celsius:
    def __init__(self,value = '37.2'):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return round(instance.C * 1.8 + 32,2)

    def __set__(self, instance, value):
        instance.C = round((float(value) - 32) / 1.8,2)

class Temperture:

    C = Celsius()
    F = Fahrenheit()


temp = Temperture()
print(temp.C)
print(temp.F)
temp.F = 100
print(temp.C)