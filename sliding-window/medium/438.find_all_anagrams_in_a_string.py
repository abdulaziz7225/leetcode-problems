"""
Problem Number: 438. Find All Anagrams in a String
Difficulty Level: Medium
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string

********************************************************************************

Given two strings s and p, return an array of all the start indices of p's anagrams in
s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""

from typing import List


# Solution 1: Sliding Window
class Solution:
    def findAnagrams(self, string: str, pattern: str) -> List[int]:
        n = len(string)
        k = len(pattern)

        result = []
        if k > n:
            return result

        pattern_freq = [0] * 26
        string_freq = [0] * 26

        for i in range(k):
            pattern_freq[ord(pattern[i]) - ord("a")] += 1
            string_freq[ord(string[i]) - ord("a")] += 1

        if string_freq == pattern_freq:
            result.append(0)

        for i in range(k, n):
            string_freq[ord(string[i]) - ord("a")] += 1
            string_freq[ord(string[i - k]) - ord("a")] -= 1

            if string_freq == pattern_freq:
                result.append(i - k + 1)

        return result

# n = len(string), k = len(pattern)
# Time Complexity: O(k + 26 * (n - k)) ==> O(n)
# Space Complexity: O(2 * 26 + n - k) ==> O(n)


# Solution 2: Optimized Sliding Window
class Solution:
    def findAnagrams(self, string: str, pattern: str) -> List[int]:
        n = len(string)
        k = len(pattern)

        result = []
        if k > n:
            return result

        pattern_freq = [0] * 26
        string_freq = [0] * 26

        for i in range(k):
            pattern_freq[ord(pattern[i]) - ord("a")] += 1
            string_freq[ord(string[i]) - ord("a")] += 1

        count = 0
        for i in range(26):
            if string_freq[i] == pattern_freq[i]:
                count += 1

        if count == 26:
            result.append(0)

        for i in range(k, n):
            left = ord(string[i - k]) - ord("a")
            right = ord(string[i]) - ord("a")

            string_freq[right] += 1
            if string_freq[right] == pattern_freq[right]:
                count += 1
            elif string_freq[right] == pattern_freq[right] + 1:
                count -= 1

            string_freq[left] -= 1
            if string_freq[left] == pattern_freq[left]:
                count += 1
            elif string_freq[left] == pattern_freq[left] - 1:
                count -= 1

            if count == 26:
                result.append(i - k + 1)

        return result

# n = len(string), k = len(pattern)
# Time Complexity: O(k + (n - k)) ==> O(n)
# Space Complexity: O(2 * 26 + n - k) ==> O(n)
