# format:
table = {'Simon': 50, 'Jack': 100, 'Rose': 150}
table1 = {'Tony': 60, 'Rafal': 80}
print('Jack: {0[Jack]:d}; Simon: {0[Simon]:d}; Rafal: {1[Rafal]:d};'.format(table, table1))


# seek
#with open('') as f:
#    f.seek()

# saving data with json
import json
v = json.dumps([1,"2",True])
print(v)