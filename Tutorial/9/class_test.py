# scope
# if no nonlocal and global , assignments do not copy data only binds names to object
# nonlocal statement live in an enclosing scope
# global statement live in the global scope
def scope_test():
    def do_local():
        spam = "local spam"
        print(f"do_local spam: {spam}")
        del spam

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
    def do_output() -> str:
        return spam

    spam = "test spam"
    do_local()
    print(f"After do local spam : {spam}")
    do_nonlocal()
    print(f"After do non local spam : {spam}")
    do_global()
    print(f"After do global spam : {spam}")
    print(f"After all check spam: {do_output()} ")

scope_test()
print(f"In global scope : {spam}")


class Warehouse(object):
    purpose = 'storage'
    region = 'west'

    def __setitem__(self, key, value):
        self.region = value + 'OK'

W1 = Warehouse()
print(W1.purpose, W1.region)

W2 = Warehouse()
W2.region = 'east'
print(W2.__class__)
print(W2.purpose, W2.region)

# private variales: start with _
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable) #define a private variales to invoke the function

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            print(f"item is {item}")
            self.items_list.append(item)

M1 = MappingSubclass(range(10))
print(M1.items_list)

# Odds and Ends : treat class as a record
class Student:
    pass

S1 = Student()
S1.name = 'john'
S1.age = 24
S1.grade = 'class 201'
print(S1.__dict__)