import pytest

from password import check_password

@pytest.mark.parametrize("passwd",[
    "Abc12345",
    "AbCD12345"
])
def test_check_password_correct(passwd):
    assert check_password(passwd) == True


@pytest.mark.parametrize("passwd",[
    "Abc1235",
    "ABC12345"
])
def test_check_password_one_failure(passwd):
    assert check_password(passwd) == False

@pytest.mark.parametrize("passwd",[
    "",
    "abdd",
    "AAAAAAAAA",
    "abc1233333"
])
def test_check_password_multiple_failure(passwd):
    assert check_password(passwd) == False
