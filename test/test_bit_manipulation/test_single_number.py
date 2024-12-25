import pytest
from src.bit_manipulation.single_number import single_number

def test_returns_boolean():

    test_input = ""
    
    result = single_number(test_input)

    assert type(result) == int