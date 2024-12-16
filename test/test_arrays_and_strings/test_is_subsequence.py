import pytest
from src.arrays_and_strings.is_subsequence import is_subsequence

def test_returns_boolean():

    s = ""
    t = ""
    
    result = is_subsequence(s,t)

    assert type(result) == bool

def test_returns_true_for_multiple_chars():

    s = "abc"
    t = "ahbgdc"
    
    result = is_subsequence(s,t)

    assert result == True

def test_returns_false_for_multiple_chars():

    s = "axc"
    t = "ahbgdc"
    
    result = is_subsequence(s,t)

    assert result == False

def test_returns_true_for_single_char():

    s = "a"
    t = "a"
    
    result = is_subsequence(s,t)

    assert result == True

def test_returns_false_for_single_char():

    s = "b"
    t = "c"
    
    result = is_subsequence(s,t)

    assert result == False

def test():

    s = "twn"
    t = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"
    
    result = is_subsequence(s,t)

    assert result == True