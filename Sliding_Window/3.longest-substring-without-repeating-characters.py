"""
Problem Number: 3. Longest Substring Without Repeating Characters
Difficulty Level: Medium
https://leetcode.com/problems/longest-substring-without-repeating-characters

********************************************************************************

Given a string s, find the length of the longest
substring
without repeating characters.
  
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
  
Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        unique_chars = set()
        curr_idx = 0
        for char in s:
            if char not in unique_chars:
                unique_chars.add(char)
                result = max(result, len(unique_chars))
            else:
                while s[curr_idx] != char:
                    unique_chars.remove(s[curr_idx])
                    curr_idx += 1
                curr_idx += 1
        return result

# k = the size of character set
# Time Complexity: O(n)
# Space Complexity: O(k)
