import pytest
from src.two_pointers.merge import merge

def test_():

    test_nums1 = [1,2,3,0,0,0]
    test_m = 3
    test_nums2 = [2,5,6]
    test_n = 3

    expected_output = [1,2,2,3,5,6]
    
    result = merge(test_nums1, test_m, test_nums2, test_n)

    assert type(result) == list