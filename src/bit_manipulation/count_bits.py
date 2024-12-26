# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/counting-bits/description/

"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i. 

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""

# 61 ms, beats 22%
# 18 MB, beats 7%

def count_bits(n):

    list_of_hamming_weights = []

    for i in range(n+1):

        binary_i = bin(i)

        count = 0

        for item in binary_i:

            if item == '1':
                count += 1

        list_of_hamming_weights.append(count)

    return list_of_hamming_weights