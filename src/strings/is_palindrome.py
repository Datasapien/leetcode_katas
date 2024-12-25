# https://algomaster.io/practice/dsa-patterns
# https://leetcode.com/problems/valid-palindrome/description/

import re

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise. 

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

# 11 ms, beats 85%
# 14 MB, beats 16%
def is_palindrome(s):

    # strip whitespace, non-alphanumeric chars and lowercase
    clean_text = ''.join(char.lower() for char in s if char.isalnum())

    return clean_text == clean_text[::-1]