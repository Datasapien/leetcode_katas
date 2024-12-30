import pytest
from src.bit_manipulation.reverse_bits import reverse_bits

def test_returns_int():

    test_input = 0b0000010100101000001111010011100
    
    result = reverse_bits(test_input)

    assert type(result) == int

def test_exanple_one():

    test_input = 0b0000010100101000001111010011100

    expected_output = 964176192
    
    result = reverse_bits(test_input)

    assert result == expected_output

def test_exanple_two():

    test_input = 0b11111111111111111111111111111101

    expected_output = 3221225471
    
    result = reverse_bits(test_input)

    assert result == expected_output