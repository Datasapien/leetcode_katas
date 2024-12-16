import pytest
from src.arrays_and_strings.is_subsequence import is_subsequence

def test_returns_boolean():

    s = "abc"
    t = "ahbgdc"
    
    result = is_subsequence(s,t)

    assert type(result) == bool