import pytest
from calculator import sum, sub, mul, div

def test_sum():
    assert sum(1,2) == 3
    assert sum(-1,2) == 1
    assert sum(-1,-2) == -3
    assert sum(0,0) == 0

def test_sub():
    assert sub(2,1) == 1
    assert sub(1,1) == 0
    assert sub(1,2) == -1
    assert sub(-1,-2) == 1

def test_mul():
    assert mul(1,2) == 2
    assert mul(-1,2) == -2
    assert mul(0,0) == 0
    assert mul(1,0) == 0

def test_div():
    assert div(1,1) == 1
    assert div(2,1) == 2
    assert div(0,1) == 0
    assert div(1,0) == "error"