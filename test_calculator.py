# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive():
    assert add(5, 3) == 8

def test_add_negative():
    assert add(-5, 3) == -2

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(2, 6) == 12

def test_divide_success():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    # Use pytest.raises to check if the ValueError is raised correctly
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)