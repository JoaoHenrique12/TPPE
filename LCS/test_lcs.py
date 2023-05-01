import pytest

from lcs import lcs

@pytest.mark.parametrize("st1, st2, size_lcs",[ 
    ("", "", 0),
    ("abc", "abc", 3),
    ("racecarer", "racecarer", 9),
    ("long", "tooth in goal", 3),
    ("abc123", "ab23ac23abc23", 5),
    ("12345","23415",4)
 ])
def test_lcs(st1, st2, size_lcs):
    assert lcs(st1, st2) == size_lcs
