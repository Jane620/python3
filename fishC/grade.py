
def isNUM(value):
    try:
        value + 1
    except TypeError:
        return False
    return  True

grade = int(input('enter your grade scores：'))

if isNUM(grade):
    if grade <= 60 and grade >= 0:
        print ('your grade score is D')
    elif grade > 60 and grade <= 80:
        print ('your grade score is C')
    elif grade > 80 and grade <= 90:
        print('your grade score is B')
    elif grade > 90 and grade <= 100:
        print('your grade score is A')
    else:
        print ('your grade score is wrong')

