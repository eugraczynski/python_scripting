import pytest
import time



def time_dec(base_func):
    def wrapper():
        start = time.time()
        a = 123
        base_func(a)
        end = time.time()
        print(f"Function '{base_func.__name__}' executed in {end - start:.10f} seconds")
        print(f"1nd decorator executed {time.time()}")
    return wrapper


@pytest.fixture(scope="function", autouse=True)
def setup_session():
    print("Setting up session resources")
    yield
    print("Tearing down session resources")


@pytest.mark.sample
@pytest.mark.usefixtures("setup_session")
@time_dec
def test_sample(x):
    assert x+2 == 2

@pytest.mark.serial
class TestClass:
    def test_method(self):
        assert "hello".upper() == "HELLO"


print(time_dec(test_sample)) # function time_dec.<locals>.wrapper


