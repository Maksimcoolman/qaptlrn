from main import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)   
