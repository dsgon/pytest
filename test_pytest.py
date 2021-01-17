import pytest

def test_passed():
    assert True

@pytest.mark.skip("Este caso no se debe ejecutar")
def test_failed():
    assert False

@pytest.mark.smoke
def test_failed_condition():
    a = 18
    b = 3
    c = a/b
    if c%2 != 0:
        pytest.fail("Este numero no es par")
    assert True

def test_skipped():
    pytest.skip()

