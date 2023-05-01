import pytest

from lcs import lcs

@pytest.mark.parametrize("st1, st2, size_lcs",[ 
    ("abc", "abc", 3)
 ])
def test_lcs(st1, st2, size_lcs):
    assert lcs(st1, st2) == size_lcs
