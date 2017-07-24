def readFile(filename):
    try:
        #sum = 1 + '1'
        f = open(filename)
        for i in f.readlines():
            print(i)
    except (FileNotFoundError,TypeError) as reason:
        print('wrong,reason is',reason)
    finally:
        f.close()
        print('wrong or not ,it\'s me')

readFile('resource/aa1.txt')

raise EOFError