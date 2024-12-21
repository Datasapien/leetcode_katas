import pytest
from src.arrays.rotate_array import rotate_array

def test_returns_list():

    test_input = []
    test_k = 1
    
    result = rotate_array(test_input, test_k)

    assert type(result) == list

def test_shifts_list_by_1():

    test_input = [1,2]
    test_k = 1
    
    expected_output = [2,1]
    
    result = rotate_array(test_input, test_k)

    assert result == expected_output