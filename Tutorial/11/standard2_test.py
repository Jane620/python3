#reprlib
import reprlib
R1 = reprlib.repr(set('fiabiu3bi fib ejnibiubib dbiueonf'))
print(R1)

# pprint: more readable
import pprint
data1 = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 3, 5], [2, 4, 6], [8, 0, 2]]]
pprint.pprint(data1, width=30)

# testwrap: show the doc fit the screen
import textwrap
doc1 = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc1, width=40))

# template: using args to change the values
import datetime
from string import Template
t1 = Template('${day} will be remenbered by ${name}')
T1 = t1.substitute(day = datetime.datetime.now(), name = "Old Wang")
print(repr(T1))

# logging
import logging
logging.info('logging info test now')

# weak reference ? this part is not done
import weakref
class A(dict):
    pass
a = A(red=1, green=2)
d = weakref.WeakKeyDictionary()
#d['primary'] = a
#print(d['primary'])

# heapq
from heapq import heapify,heappop,heappush
data2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data2) # rearrange list to heap order
#       0
#    1     2
#  6   3 5    4
# ..  .. ..   ..
# access a parent/child node with indices
#i is the index of the list ,begins with 1
#A root node｜i = 1, the first item of the array
#A parent node｜parent(i) = i / 2
#A left child node｜left(i) = 2i
#A right child node｜right(i)=2i+1
heappush(data2, -5)
print(data2)