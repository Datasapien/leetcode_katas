import pytest
from src.arrays_and_strings.producet_except_self import product_except_self

def test_returns_list():

    test_input = []
    
    result = product_except_self(test_input)

    assert type(result) == list