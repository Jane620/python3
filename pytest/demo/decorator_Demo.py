

def decorator(func,*args) -> int:
    print("Enter decorator")
    return lambda :func() / 12


@decorator
def funct() -> int:
    print("Enter funct")
    return 24


if __name__ == '__main__':
    print(funct())
