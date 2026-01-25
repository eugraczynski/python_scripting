import pytest
import time


@pytest.fixture(scope="function")
def setup_function():
    print("Function-level setup")
    yield

# @pytest.fixture(scope="class")
# def setup_function():
#     print("Class-level setup")
#     yield

# @pytest.fixture(scope="session")
# def setup_function():
#     print("Session-level setup")
#     yield

def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )

# @time_dec # decorator is not globally available
# TODO: find a way to share decorators across project
def time_dec(base_func):
    def wrapper():
        start = time.time()
        base_func()
        end = time.time()
        print(f"Function '{base_func.__name__}' executed in {end - start:.10f} seconds")
    return wrapper


