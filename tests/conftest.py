import pytest
import time


@pytest.fixture(scope="session")
def setup_session():
    print("Setting up session resources")
    yield



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


