import pytest


testdata = [
    (1, 2),(3, 4),(5, 6)]

@pytest.mark.sample
@pytest.mark.debug
@pytest.mark.usefixtures("setup_function")
@pytest.mark.parametrize("x,y", testdata)
# def test_sample(x=1, expected=2):     # throws error: function already takes
# an argument 'x' with default value
#     assert x + 1 == expected
def test_sample(x, y):
    assert x + 1 == y