import pytest
from src.arrays.remove_duplicates import remove_duplicates

def test_returns_int():
    test_input = [0]

    result = remove_duplicates(test_input)

    assert type(result) == int

def test_example_one():
    test_input = [1,1,2]

    expected_output = 2

    result = remove_duplicates(test_input)

    assert result == expected_output

def test_example_two():
    test_input = [0,0,1,1,1,2,2,3,3,4]

    expected_output = 5

    result = remove_duplicates(test_input)

    assert result == expected_output

def test_():
    test_input = [1,1,2]

    expected_output = 2

    result = remove_duplicates(test_input)

    assert result == expected_output