
import pytest

def f():
    raise SystemError(1)
def f2():
    raise ValueError("no support")

def test_mytest():
    with pytest.raises(SystemError):
        f()
    with pytest.raises(ValueError):
        f2()