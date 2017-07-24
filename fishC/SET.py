#假设一个列表中存在重复的数值，如何通过一般的方式处理
#可以采用简单的方式，set

def DelRepeat(list):
    temp=[]
    for each in list:
        if each not in temp:
            temp.append(each)
        #print(temp)
    return temp

list_A = [1,4,3,5,2,1,3,1,3,45,5]
list_2 = DelRepeat(list_A)
print(list_2)

list_3 = list(set(list_A))
print(list_3)