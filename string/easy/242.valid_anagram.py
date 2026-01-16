"""
Problem Number: 242. Valid Anagram
Difficulty Level: Easy
https://leetcode.com/problems/valid-anagram

********************************************************************************

Given two strings s and t, return true if t is an
anagram
of s, and false otherwise.
  
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
  
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
  Follow up: What if the inputs contain Unicode characters? How would you adapt your
  solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1

        for char in letters:
            if char != 0:
                return False
        return True

# n = len(s), k = 26
# Time Complexity: O(n + 2 * k) ==> O(n)
# Space Complexity: O(k) ==> O(1)
