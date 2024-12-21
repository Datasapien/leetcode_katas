import pytest
from src.arrays.max_profit import max_profit

def test_returns_list():

    test_input = []
    
    result = max_profit(test_input)

    assert type(result) == int

def test_returns_zero_for_descending_prices():

    test_input = [4,3,2,1]

    expected_output = 0
    
    result = max_profit(test_input)

    assert result == expected_output

def test_returns_max_profit_max_after_min():

    test_input = [2,5,4,3,7]

    expected_output = 5
    
    result = max_profit(test_input)

    assert result == expected_output