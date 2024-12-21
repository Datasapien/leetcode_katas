import pytest
from src.arrays.move_zeroes import move_zeroes

def test_returns_list():
    test_input = [0]

    result = move_zeroes(test_input)

    assert type(result) == list

def test_reorders_list_for_simple_list():
    test_input = [0,1]

    result = move_zeroes(test_input)

    expected_output = [1,0]

    assert result == expected_output

def test_preserves_order_for_simple_list():
    test_input = [1,0]

    result = move_zeroes(test_input)

    expected_output = [1,0]

    assert result == expected_output 

def test_reorders_for_test_list():
    test_input = [0,1,0,3,12]

    result = move_zeroes(test_input)

    expected_output = [1,3,12,0,0]

    assert result == expected_output

def test_preserves_order_for_negative_numbers():
    test_input = [-12,1,3,0,0]

    result = move_zeroes(test_input)

    expected_output = [-12,1,3,0,0]

    assert result == expected_output 

def test_reorders_for_negative_numbers():
    test_input = [0,1,3,0,0,-12]

    result = move_zeroes(test_input)

    expected_output = [1,3,-12,0,0,0]

    assert result == expected_output

def test_():
    test_input = [0,1,0,3,12]

    result = move_zeroes(test_input)

    expected_output = [1,3,12,0,0]

    assert result == expected_output

def test_changes_made_in_place():

    test_input = [0,1]

    result = move_zeroes(test_input)

    expected_output = [1,0]

    assert result == expected_output
    assert result is test_input