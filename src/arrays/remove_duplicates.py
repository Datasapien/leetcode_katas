# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

# Solution passes tests, but doesn't remove duplicates in-place therefore fails other test criteria ..

def xremove_duplicates(nums):

    result = len(list(set(nums)))

    return result

def remove_duplicates(nums):

    unique = 0

    for i in range(1, len(nums)):

        if nums[i] != nums[unique]:

            unique += 1
            nums[unique] = nums[i]

    return unique + 1