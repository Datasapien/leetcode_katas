import pytest
from src.bit_manipulation.single_number import single_number

def test_returns_int():

    test_input = [1,2,1,2,3]
    
    result = single_number(test_input)

    assert type(result) == int

def test_for_single_num():

    test_input = [1]

    expected_output = 1
    
    result = single_number(test_input)

    assert result == expected_output

def test_for_single_three_nums():

    test_input = [2,2,1]

    expected_output = 1
    
    result = single_number(test_input)

    assert result == expected_output

def test_for_single_five_nums():

    test_input = [4,1,2,1,2]

    expected_output = 4
    
    result = single_number(test_input)

    assert result == expected_output