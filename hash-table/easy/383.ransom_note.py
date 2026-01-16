"""
Problem Number: 383. Ransom Note
Difficulty Level: Easy
https://leetcode.com/problems/ransom-note

********************************************************************************

Given two strings ransomNote and magazine, return true if ransomNote can be constructed
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
  
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
  
Constraints:
1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = [0] * 26

        for char in magazine:
            magazine_counter[ord(char) - ord('a')] += 1

        for char in ransomNote:
            idx = ord(char) - ord('a')
            if magazine_counter[idx] == 0:
                return False
            magazine_counter[idx] -= 1

        return True

# n = len(ransomNote), m = len(magazine)
# Time Complexity: O(n + m)
# Space Complexity: O(26) ==> O(1)
