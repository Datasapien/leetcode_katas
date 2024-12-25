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

    test_input = [2,7,4,3,6]

    expected_output = 5
    
    result = max_profit(test_input)

    assert result == expected_output

def test_returns_zero_max_before_min():

    test_input = [10,6,5,4,3]

    expected_output = 0
    
    result = max_profit(test_input)

    assert result == expected_output

def test_returns_profix_max_before_min():

    test_input = [10,6,7,8,9]

    expected_output = 3
    
    result = max_profit(test_input)

    assert result == expected_output

def test_returns_zero_for_no_profit():

    test_input = [7,6,4,3,1]

    expected_output = 0
    
    result = max_profit(test_input)

    assert result == expected_output

def test_returns_max_profit_if_min_after_max():

    test_input = [2,4,1]

    expected_output = 2

    result = max_profit(test_input)

    assert result == expected_output