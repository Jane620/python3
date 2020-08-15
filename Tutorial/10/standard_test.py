
# os
# shutil: shell tool utils
import shutil, os
os.remove('data3.db')
shutil.copyfile('data.db', 'dir/data2.db')
shutil.move('dir/data2.db', 'data3.db')

# glob : list the pattern from the path
import glob
G1 = glob.glob('*.db')
print(G1)

import sys
print(sys.argv)

# re: string pattern matching
import re
match1 = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(match1)
# \number Matches the contents of the group of the same number.
match2 = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(match2)
match3 = re.findall(r'(\b[a-z]+) \1', 'cat in the the hat') # it matchs 'the the', but not 'thethe', a space befor \1
print(match3)
match4 = re.findall(r'\b ', 'cat in the the hat')
print(match4)

# random
import random
for i in range(5):
    C1 = random.choice(range(5))
    print(C1)

# statistics
import statistics
data = list(range(6))
D1 = statistics.mean(data) # get average value
D2 = statistics.median(data) # get the middle value
D3 = statistics.variance(data) # get variance value
print(data)
print(D1, D2, D3)

# doctest: to test the example in the docstrings
import doctest
def avg(value):
    """ computes the mean of a list

    >>> print(avg([20,30]))
    25.0
    """
    return sum(value) / len(value)
X1 = doctest.testmod()
print(X1)

# unittest
