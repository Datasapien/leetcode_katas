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

# X ms, beats X
# Y MB, beats Y
def longest_common_prefix(strings):

    strings.sort()
    first_word = strings.pop(0)
    prefix = ""

    for i in range(len(first_word)):

        match_count = 0

        for j in range(len(strings)):

            if strings[j][i] == first_word[i]:
                
                match_count += 1
        
            j += 1

        if match_count == len(strings):
            prefix +=  first_word[i]

        i += 1

    return prefix