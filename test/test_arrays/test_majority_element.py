import pytest
from src.arrays_and_strings.majority_element import majority_element

def test_returns_int():
    test_input = [0]

    result = majority_element(test_input)

    assert type(result) == int

def test_returns_majority_element_short_list():
    test_input = [3,2,3]
    expected_output = 3

    result = majority_element(test_input)

    assert result == expected_output

def test_returns_majority_element_longer_list():
    test_input = [2,2,1,1,1,2,2]
    expected_output = 2

    result = majority_element(test_input)

    assert result == expected_output

def test_returns_element_large_num():
    test_input = [3,3,4]
    expected_output = 3

    result = majority_element(test_input)

    assert result == expected_output