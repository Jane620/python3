#-*- coding:utf-8 -*-

while True:
    reply = input("enter a word:")
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except ValueError:
        print('not a number')
    # 此处的else同try结合，并非为上面if
    else:
        print(int(reply)**2)

print('bye')