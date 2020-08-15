def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotation:", f.__annotations__)
    print("Args:", ham, eggs)
    return ham + " add " + eggs

f("spam")