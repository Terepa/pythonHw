import pytest

def calculator(operation, a, b):
    if operation == "sum":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        raise ValueError("unknown operation")

# write the test cases for above method

@pytest.mark.parametrize("operation, a, b, exp", [
    ("sum", 1, 2, 3),
    ("sub", 3, 4, -1),
    ("mul", 5, 6, 30),
    ("div", 7, 7, 1)
], ids=["sum", "sub", "mul", "div"])
def test(operation, a, b, exp):
        res = calculator(operation, a, b)
        assert res == exp, f"Incorrect result: operation {operation}, values {a}, {b} expected result: {exp} real result: {res}"

def test_operation_error():
    with pytest.raises(ValueError):
        calculator("test", 1, 3)

@pytest.mark.parametrize("operation, a, b, exp_error", [
    ("str", 1, 2, ValueError),
    ("div", "str", 4, ValueError),
    ("div", 1, 0, ZeroDivisionError),
    ("sum", "t1", "t2", ValueError),
    ("mul", 1, "str", ValueError)
], ids=["01", "02", "zero", "string_sum", "string_mul"])


def test_wrong_string(operation, a, b, exp_error):
    with pytest.raises(exp_error):
        calculator(operation, a, b)

