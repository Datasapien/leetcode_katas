import pytest
from src.arrays_and_strings.product_except_self import product_except_self

def test_returns_list():

    test_input = []
    
    result = product_except_self(test_input)

    assert type(result) == list

def test_returns_correct_for_three_items():

    test_input = [1,2,3]

    expected_result = [6,3,2]
    
    result = product_except_self(test_input)

    assert result == expected_result

def test_returns_correct_empty_list():

    test_input = []

    expected_result = []
    
    result = product_except_self(test_input)

    assert result == expected_result

def test_returns_correct_for_two_items():

    test_input = [1,2]

    expected_result = [2,1]
    
    result = product_except_self(test_input)

    assert result == expected_result

def test_returns_correct_for_example_one():

    test_input = [1,2,3,4]

    expected_result = [24,12,8,6]
    
    result = product_except_self(test_input)

    assert result == expected_result

def test_returns_correct_for_example_two():

    test_input = [-1,1,0,-3,3]

    expected_result = [0,0,9,0,0]
    
    result = product_except_self(test_input)

    assert result == expected_result