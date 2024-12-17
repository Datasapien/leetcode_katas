import pytest
from src.arrays_and_strings.longest_common_prefix import longest_common_prefix

def test_returns_str():

    test_input = ["a", "ab", "abc"]
    
    result = longest_common_prefix(test_input)

    assert type(result) == str

def test_returns_empty_str_for_no_prefix():

    test_input = ["a", "b", "c"]

    expected_output = ""
    
    result = longest_common_prefix(test_input)

    assert result == expected_output

def test_returns_correct_prefix_for_single_chars():

    test_input = ["a", "a", "a"]

    expected_output = "a"
    
    result = longest_common_prefix(test_input)

    assert result == expected_output

def test_returns_correct_prefix_for_multiple_chars():

    test_input = ["abcd", "abc", "abcde"]

    expected_output = "abc"
    
    result = longest_common_prefix(test_input)

    assert result == expected_output