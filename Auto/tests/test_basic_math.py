from src.math_utils import multiplay


def test_basic_math():
    assert 2 + 2 == 4

def test_multiply():
    assert multiplay(3,5), "Функция отработал не правильно"