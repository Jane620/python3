
list_example = list(range(5))

print(list_example)
# pop : arg is the index
list_example.pop(1)
print(f"pop list is :{list_example}")

# index
index = list_example.index(3)
print(f"index of list 3 is :{index}")

# reverse
list_example.reverse()

# clear
print(f"clear list start as :{list_example}")
list_example.clear()
print(f"clear list is :{list_example}")

# last-in ,first-out
list_example.append(1)
list_example.append(2)
list_example.append(3)
list_example.pop()
print(f"last-in and first-out line is {list_example}")

# first-in, first-out
from collections import deque
queue = deque(list(range(5)))
queue.append(5)
queue.append(6)
queue.popleft()
print(f"first-in and first-out line is {queue}")

# Nested list
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

result = []
for i in range(4):
    result_2 = []
    for row in matrix:
        result_2.append(row[i])
        print(f"this is inner list {row}")
    result.append(result_2)
    print(f"this is outer list: {result}")

# or operator
# return the fist value that equals to true
str1, str2, str3 = False, "", True
rest_1 = str1 or str2 or str3
rest_1