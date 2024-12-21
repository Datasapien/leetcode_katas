# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/longest-common-prefix/description/

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "". 

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# 1 ms, beats 46%
# 13 MB, beats 14%
def longest_common_prefix(strs):

    if not strs:
        return ""

    sorted_list = sorted(strs, key=len)
    shortest_word = sorted_list.pop(0)

    prefix = ""

    for i in range(len(shortest_word)):

        match_count = 0

        for j in range(len(sorted_list)):

            if sorted_list[j][i] == shortest_word[i]:
                
                match_count += 1
        
            j += 1

        if match_count == len(sorted_list) and i == len(prefix):
            prefix += shortest_word[i]

        i += 1

    return prefix

# 0 ms, beats 100%
# 13 MB, beats 5%
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix