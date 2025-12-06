"""
Problem Number: 49. Group Anagrams
Difficulty Level: Medium
https://leetcode.com/problems/group-anagrams

********************************************************************************

Given an array of strings strs, group the
anagrams
together. You can return the answer in any order.
  
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
  
Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for text in strs:
            anagrams[self.ascii_tuple(text)].append(text)
        return list(anagrams.values())

    def ascii_tuple(self, text):
        letters = [0] * 26
        for char in text:
            letters[ord(char) - ord('a')] += 1
        return tuple(letters)

# n = len(strs), m is the length longest string
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
