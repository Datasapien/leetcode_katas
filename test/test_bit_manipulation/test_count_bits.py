import pytest
from src.bit_manipulation.count_bits import count_bits

def test_returns_int():

    test_input = 1
    
    result = count_bits(test_input)

    assert type(result) == list

def test_example_one():

    test_input = 2

    expected_output = [0,1,1]
    
    result = count_bits(test_input)

    assert result == expected_output

def test_example_two():

    test_input = 5

    expected_output = [0,1,1,2,1,2]
    
    result = count_bits(test_input)

    assert result == expected_output