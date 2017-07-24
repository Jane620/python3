def fab(max):
    n,a,b= 0,0,1
    if n < max:
        yield b
        a,b = b,a+b
        n = n + 1

f= fab(5)
print(f.__next__)

