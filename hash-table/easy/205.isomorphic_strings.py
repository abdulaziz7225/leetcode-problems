"""
Problem Number: 205. Isomorphic Strings
Difficulty Level: Easy
https://leetcode.com/problems/isomorphic-strings

********************************************************************************

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a
character may map to itself.
  
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
  
Constraints:
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for idx in range(len(s)):
            char_s = s[idx]
            char_t = t[idx]

            if char_s not in s_to_t:
                s_to_t[char_s] = char_t

            if t[idx] not in t_to_s:
                t_to_s[char_t] = char_s

            if s_to_t[char_s] != char_t or t_to_s[char_t] != char_s:
                return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(128) for ASCII characters ==> O(1)
