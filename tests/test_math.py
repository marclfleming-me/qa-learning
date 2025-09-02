import pytest

def add(a: int, b: int) -> int:
    """Simple addition function for demo purposes."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Simple subtraction function for demo purposes."""
    return a - b

# --------------------
# Tests start here
# --------------------

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -5) == -6

def test_subtract_result_positive():
    assert subtract(10, 3) == 7

def test_subtract_result_negative():
    assert subtract(3, 10) == -7

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 5, 5),
    (-2, -3, -5),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
