#-*- coding:utf-8 -*-

main_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#列表推导器
dialog = [main_list[i][i] for i in [0, 1, 2]]
print(dialog)

#生成器generator ，同列表推导差距为一个是[],一个为()
generator = (sum(i) for i in main_list)
print(next(generator))
print(next(generator))
print(next(generator))
#print(next(generator))

#map 对
sum_list = map(sum, main_list)
print(list(sum_list))

#计算每一个子列表的合计
sum_list2 = {i:sum(main_list[i]) for i in range(len(main_list))}
print(sum_list2)