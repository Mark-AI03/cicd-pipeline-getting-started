from src.main import add
from src.main import substract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(5, 5) == 10


def test_substract():
    assert substract(5, 3) == 2
    assert substract(0, 0) == 0
    assert substract(-1, -1) == 0
    assert substract(10, 5) == 5