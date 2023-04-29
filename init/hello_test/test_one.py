import pytest

@pytest.mark.nomark
def test_no_mark():
    assert "U" == "u".upper()

@pytest.mark.boolean
def test_always_passe():
    assert True

@pytest.mark.integer
def test_number_in():
    assert 3 in [1,2,4,3]


@pytest.mark.boolean
@pytest.mark.return_error
def test_always_fail():
    assert False

@pytest.mark.return_error
def test_raise():
    raise ValueError("Number must be even")
