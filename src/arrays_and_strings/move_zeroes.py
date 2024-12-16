# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/move-zeroes/description/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# 3ms, beats 90.22%
def move_zeroes(nums):

    non_zero_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos] = nums[i]
            non_zero_pos += 1

    for i in range(non_zero_pos, len(nums)):
        nums[i] = 0

    return nums

# 11ms, beats 39.48%
def move_zeroes(nums):

    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]

        if nums[slow] != 0:
            slow += 1

    return nums