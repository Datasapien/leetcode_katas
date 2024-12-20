# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/rotate-array/description/
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. 

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
"""

# GPT solution
# 4 ms, beats 58%
# 23 MB, beats 28%

def rotate_array(nums, k):

    k = k % len(nums)

    last_k_elements = nums[:-k]
    first_k_elements = nums[-k:]

    #Ensures original list updated in place
    nums[:] = first_k_elements + last_k_elements

    return nums