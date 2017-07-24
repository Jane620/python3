#record.txt对话进行分割
#对话A保存为boy_*.txt，对话B保存为girl_*.txt
#不同对话间采用====分割了
#首字母匹配  if s.startwiths('')

count = 1
filename_a = 'boy_'+str(count)+'.txt'
filename_b = 'boy_'+str(count)+'.txt'

f = open('record.txt')


for each_line in f.readlines():
    #通过判断
    if each_line.startswith('PersonA'):
        s_a = str(each_line.strip().split(':')[1:])
        #SA = open(filename_a ,'w')
        #SA.writelines(s_a)
        #SA.close()
        print('SA:',s_a,end='')
    elif each_line.startswith('PersonB'):
        s_b = each_line
        #print('SB:',each_line,end='')
    elif each_line.startswith('=='):
        s_c = each_line
        #print('SC:',each_line,end='')

f.close()