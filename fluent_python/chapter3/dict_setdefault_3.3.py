# -*- coding:UTF-8 -*-

import sys
import re

#出现多次字母数字下划线中文[^A-Za-z0-9_]的正则表达式
WORD_RE = re.compile(r'\d+')

index = {}
#sys.argv[0] 实际为该py所在的绝对路径,因此例如dict_setdefault_3.3.py aaalbb，则表明argv[1] = aaalbb
with open(sys.argv[0],encoding='utf-8') as fp:
    #enumerate将fp读取的每一行都重新组合成一个元祖，按照1的顺序开始,
    for line_no,line in enumerate(fp,1):
        #re.finditer返回匹配结果的迭代器
        for match in WORD_RE.finditer(line):
            #match.group返回匹配的子集
            word = match.group()
            print("word:",word)
            #返回match_group中index的编号
            column_no = match.start()+1
            #location为实际匹配内容对应的行数和列数
            location = (line_no,column_no)
            #不建议这样写
            occurrences = index.get(word,[])
            occurrences.append(location)
            index[word] = occurrences
#因字母形式打印结果
for word in sorted(index,key=str.upper):
    print(word,index[word])

