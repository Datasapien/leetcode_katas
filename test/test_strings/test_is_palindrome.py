import pytest
from src.strings.is_palindrome import is_palindrome

def test_returns_boolean():

    s = ""
    
    result = is_palindrome(s)

    assert type(result) == bool

def test_all_lower_case_palindrome():

    s = "dad"

    expected_output = True
    
    result = is_palindrome(s)

    assert result == expected_output

def test_all_upper_case_palindrome():

    s = "DAD"

    expected_output = True
    
    result = is_palindrome(s)

    assert result == expected_output

def test_whitespace_palindrome():

    s = "da d"

    expected_output = True
    
    result = is_palindrome(s)

    assert result == expected_output

def test_whitespace_upper_non_alpha_palindrome():

    s = "%Da d"

    expected_output = True
    
    result = is_palindrome(s)

    assert result == expected_output

def test_whitespace_non_palindrome():

    s = "%Dab d"

    expected_output = False
    
    result = is_palindrome(s)

    assert result == expected_output