# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/product-of-array-except-self/description/
import math
import functools
import operator

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation. 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

# These solutions work, but times out for larger lists :(

def xproduct_except_self(nums):

    new_nums = []

    for i in range(len(nums)):

        multiplier = 1

        list_to_multiply = nums[i+1:] + nums[:i]

        for item in list_to_multiply:
            multiplier *= item
        
        new_nums.append(multiplier)

    return new_nums

def xproduct_except_self(nums):

    new_nums = []

    for i in range(len(nums)):

        list_to_multiply = nums[i+1:] + nums[:i]

        new_nums.append(math.prod(list_to_multiply))

    return new_nums

def xproduct_except_self(nums):

    new_nums = []

    for i in range(len(nums)):

        list_to_multiply = nums[i+1:] + nums[:i]

        new_nums.append(functools.reduce(operator.mul, list_to_multiply))

    return new_nums

# From our good friend AI
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    # Compute prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Compute suffix products and multiply with prefix
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
