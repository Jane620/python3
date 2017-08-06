#-*- coding:utf-8 -*-


word = 'spam'

for (offset,str) in enumerate(word):
    print(offset,str)

list_word = [ c*i for c,i in enumerate(word)]
print(list_word)