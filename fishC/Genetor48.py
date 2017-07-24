test = {'aa':11,'bb':22,'cc':33}

for each in test:
    print('{0}->{1}'.format(each,test[each]))

test2 = 'good'
it = iter(test2)
while True:
    try:
        each = next(it)
    except StopIteration as e:
        break
    print(each)