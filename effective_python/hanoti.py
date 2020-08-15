

def hanoti(n, x, y, z):

    if n == 0:
        pass
        #print("why it's over")
    else:
        hanoti(n-1, x, z, y)
        print(f"{x} -> {y}")
        hanoti(n-1, z, x, y)


def more_add(n):

    result = 0
    if n == 0:
        result += 0
    else:
        result = n + more_add(n-1)
    return result

if __name__ == '__main__':
    #hanoti(6, "A", "B", "C")
    print(more_add(10))