import pytest
from src.bit_manipulation.hamming_weight import hamming_weight

def test_returns_int():

    test_input = 1
    
    result = hamming_weight(test_input)

    assert type(result) == int

def test_example_one():

    test_input = 11

    expected_output = 3
    
    result = hamming_weight(test_input)

    assert result == expected_output