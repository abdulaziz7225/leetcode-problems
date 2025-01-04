"""
Problem Number: 1930. Unique Length-3 Palindromic Subsequences
Difficulty Level: Medium
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

********************************************************************************

Given a string s, return the number of unique palindromes of length three that are a subsequence of s. Note that even if 
there are multiple ways to obtain the same subsequence, it is still only counted once. A palindrome is a string that 
reads the same forwards and backwards. A subsequence of a string is a new string generated from the original string with 
some characters (can be none) deleted without changing the relative order of the remaining characters. For example, "ace"
is a subsequence of "abcde".
 
Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:
Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:
Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")

Constraints:
3 <= s.length <= 10^5
s consists of only lowercase English letters.
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_and_last = dict()
        for idx, char in enumerate(s):
            if char in first_and_last:
                first_and_last[char][1] = idx
            else:
                first_and_last[char] = [idx, idx]

        result = 0
        for char, val in first_and_last.items():
            if val[0] + 1 < val[1]:
                unique_chars = set()
                for i in range(val[0]+1, val[1]):
                    unique_chars.add(s[i])
                result += len(unique_chars)
        return result
        