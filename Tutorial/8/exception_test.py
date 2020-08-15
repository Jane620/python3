# try / except
# execute the statment between try and exception
# if no exception occurs ,then skip the exception clause
# if an exceptions occurs , then check if it matches the exception named after exception keyword ,then execute exception
# if an exceptions occurs , then check if it does not matches, then it is an unhandled exceptions
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# finally: whatever there is an exception, it will be executed before the try statement completesd
# but if catches an exception, the finally will after exception
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print('catch exceptions')
finally:
    print('Good finally')