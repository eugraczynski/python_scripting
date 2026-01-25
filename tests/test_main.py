import pytest
import time




@pytest.mark.sample
@pytest.mark.usefixtures("setup_function") # using fixture from conftest.py
def test_sample(x=1):
    assert x + 1 == 2

@pytest.mark.serial
@pytest.mark.classy
@pytest.mark.sample
class TestClass:
    def test_method(self):
        assert "hello".upper() == "HELLO"

    @pytest.mark.sample(marked_as="smoke")
    def test_method_two(self):
        assert "phased".upper() == "PAHSED"

    @pytest.mark.inClassy
    def test_method_in_Classy(self):
        assert "hello".upper() == "HELLsO"


@pytest.mark.other
class TestClassOther:
    def test_method(self):
        assert "hello".upper() == "mda"

# @pytest.mark.parametrize("input,expected", [(1, 2), (3, 4), (5, 6)])
# def test_param(input, expected):
#     assert input + 2 == expected


# @time_dec # decorator is not globally available
# TODO: find a way to share decorators across project
def time_dec(base_func):
    def wrapper():
        start = time.time()
        a = 123
        base_func(a)
        end = time.time()
        print(f"Function '{base_func.__name__}' executed in {end - start:.10f} seconds")
        print(f"1nd decorator executed {time.time()}")
    return wrapper

print(time_dec(test_sample)) # function time_dec.<locals>.wrapper


