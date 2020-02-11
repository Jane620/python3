

def decorator(func,*args):
    return lambda :func() / 12


@decorator
def funct() -> int:
    return 12


if __name__ == '__main__':
    print(funct())
