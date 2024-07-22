import pytest
import ruamel
from src.calc_demo import *

def test_calc():
    a = 10
    b = 0
    with pytest.raises(ValueError):
        div(a,b)

    c = add(a,b)
    assert c == 10
