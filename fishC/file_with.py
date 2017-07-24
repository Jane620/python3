try:
    with open('resource/aa.txt','r') as f:
    # f = open('resource/aa.txt')
        for i in f:
            print(i)
except OSError :
    print('exceptions')
#finally:
#    f.close()

