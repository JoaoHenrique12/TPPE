import pytest

from . import MAX_HEALTH
from .character import character


@pytest.mark.parametrize("initial_health, amount, expected_health",[ 
    (1, MAX_HEALTH - 1, MAX_HEALTH),
    (MAX_HEALTH - 2,  1, MAX_HEALTH - 1),
    (MAX_HEALTH, MAX_HEALTH , MAX_HEALTH),
 ])
def test_sum_health(initial_health, amount, expected_health):
    char = character(health=initial_health)
    char.sum_health(amount)
    assert char.health == expected_health

@pytest.mark.parametrize("initial_health, amount, expected_health",[ 
    (1, 1, 0),
    (2,  1, 1),
    (1, MAX_HEALTH , 0),
 ])
def test_reduce_health(initial_health, amount, expected_health):
    char = character(health=initial_health)
    char.reduce_health(amount)
    assert char.health == expected_health

@pytest.mark.parametrize("amount", [ -2, -3, -8 ])
def test_amount_value_error(amount):
    char = character()
    with pytest.raises(ValueError):
        char.amount = amount

@pytest.mark.parametrize("amount", [ -2.3, "", {} ])
def test_amount_type_error(amount):
    char = character()
    with pytest.raises(TypeError):
        char.amount = amount
