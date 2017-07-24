record = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]
def printFoo(x,y):
    print ('foo',x,y)
def printBar(s):
    print('bar',s)
for tag, *argvs in record:
    if tag == 'foo':
        printFoo(*argvs)
    elif tag == 'bar':
        printBar(*argvs)
    else:
        print('no match')