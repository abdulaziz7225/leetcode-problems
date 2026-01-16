"""
Problem Number: 387. First Unique Character in a String
Difficulty Level: Easy
https://leetcode.com/problems/first-unique-character-in-a-string

********************************************************************************

Given a string s, find the first non-repeating character in it and return its index. If
it does not exist, return -1.
  
Example 1:
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
  
Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.
"""

from collections import defaultdict


# Solution 1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1

        for idx, char in enumerate(s):
            if counter[char] == 1:
                return idx

        return -1

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(26) ==> O(1)


# Solution 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = len(s)

        for i in range(26):
            letter = chr(i + ord('a'))
            first_occurrence = s.find(letter)
            if first_occurrence != -1 and first_occurrence == s.rfind(letter):
                position = min(position, first_occurrence)

        return position if position != len(s) else -1

# Time Complexity: O(26 * n) ==> O(n)
# Space Complexity: O(1)
