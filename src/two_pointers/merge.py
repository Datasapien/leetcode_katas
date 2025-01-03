# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/merge-sorted-array/description/

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

# 0 ms, beats 100%
# 12 MB, beats 21%
# This code works, but uses .sort() - use pointers instead :')

def xmerge(nums1, m, nums2, n):

    for i in range(n):

        nums1[m+i] = nums2[i]

    nums1.sort()
        
    return nums1

"""
Three pointers: i, j and k
i points to last digit of nums1 (before all the 0s)
j points to last digit of nums2
k points to last index of nums1 (final 0)

Need to find which value will fill the last position: the value at nums1[i] or nums2[j]. Once found, populate nums1[k] with this value and decrement k and i/j (whichever was larger). Repeat until all values in nums2 have been compared (ie until j = -1)
"""

# 0 ms, beats 100%
# 13 MB, beats 13%

def merge(nums1, m, nums2, n):

    i = m -1
    j = n -1
    k = m + n - 1

    while j >= 0:

        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    return nums1