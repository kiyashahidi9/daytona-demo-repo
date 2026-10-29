import pytest

from calc.operations import modulo


def test_modulo():
    assert modulo(10, 3) == 1


def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        modulo(1, 0)
