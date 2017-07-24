list_a= [x for x in range(10) if x %2 != 0]
list_b = [1,3,5,7,9]
dict_a={}.fromkeys(range(len(list_a)),0)
dict_b = {}.fromkeys(list_b,0)
print(list_a)
print(dict_b)
print(dict_a)
print(range(len(list_a)))
print({}.fromkeys(range(0,5),0))