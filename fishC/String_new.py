class String1(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls,string)

s = String1('aa')
print(s)