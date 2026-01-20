import pytest

@pytest.mark.sample
@pytest.mark.usefixtures("setup_session")
def test_sample(x=1):
    assert x + 1 == 2