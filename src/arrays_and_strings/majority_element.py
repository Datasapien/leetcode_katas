# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/majority-element/description/

"""
Given an array nums of size n, return the majority element. 
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

# 4ms, beats 79.95%
# 13.18 MB, beats 42.84%
def majority_element(nums):

    max_occurences = 1
    majority_element = nums[0]

    num_set = set(nums)

    for number in num_set:
        if nums.count(number) > max_occurences:
            majority_element = number
            max_occurences = nums.count(number)        
    
    return majority_element

# Boyer-Moore Majority Vote Algorithm
# 5 ms, beats 76%
# 14 MB, beats 5%
def majority_element(nums):
    count = 0
    majority = 0

    for i in range(len(nums)):
        if count == 0 and majority != nums[i]:
            majority = nums[i]
            count += 1
        elif majority == nums[i]:
            count += 1
        else:
            count -= 1
    
    return majority