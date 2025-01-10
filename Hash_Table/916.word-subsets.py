"""
Problem Number: 916. Word Subsets
Difficulty Level: Medium
https://leetcode.com/problems/word-subsets

********************************************************************************

You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order.
  
Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
  
Constraints:
1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = {}
        for word in words2:
            for char in word:
                count = word.count(char)
                if char not in max_freq or count > max_freq[char]:
                    max_freq[char] = count

        result = []
        for word in words1:
            for char, freq in max_freq.items():
                if word.count(char) < freq:
                    break
            else:
                result.append(word)
        return result

# n = len(words1), k = length of a word in words1
# m = len(words2), l = average length of a word in words2
# Time Complexity: O(n * k + m * l^2)
# Space Complexity: O(n)
