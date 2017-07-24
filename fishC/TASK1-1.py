def saveFile(boy,girl,count):
    filename_boy = 'boy_' + str(count) + '.txt'
    filename_girl = 'girl_' + str(count) + '.txt'
    boy_file = open(filename_boy, 'w')
    girl_file = open(filename_girl, 'w')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

def split_file(filename):
    f = open(filename)
    boy=[]
    girl=[]
    # 按照==分割，作为计算器来保存对应的文件名
    count = 1
    for each in f:
        if not each.startswith('===='):
            (role,line) = each.strip().split(':',1)
            if role == 'PersonA':
                boy.append(line)
            elif role == 'PersonB':
                girl.append(line)
        else:
            saveFile(boy,girl,count)
            boy = []
            girl= []
            count += 1
    f.close()

split_file('record.txt')