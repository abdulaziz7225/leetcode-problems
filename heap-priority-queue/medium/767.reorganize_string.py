"""
Problem Number: 767. Reorganize String
Difficulty Level: Medium
Link: https://leetcode.com/problems/reorganize-string/

********************************************************************************

Given a string s, rearrange the characters of s so that any two adjacent characters are
not the same. Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

from heapq import heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = dict()
        for char in s:
            count[char] = count.get(char, 0) + 1

        max_heap = []
        for char, freq in count.items():
            heappush(max_heap, (-freq, char))

        prev_char = ""
        prev_freq = 0
        result = []

        while max_heap:
            freq, char = heappop(max_heap)
            result.append(char)
            if prev_freq < 0:
                heappush(max_heap, (prev_freq, prev_char))

            freq += 1
            prev_char = char
            prev_freq = freq

        if len(result) != len(s):
            return ""
        return "".join(result)

# n = len(s), m = number of unique characters
# Time Complexity: O(n + (n + m) * log(m)) ==> O(n * log(m))
# Space Complexity: O(n + 2 * m) ==> O(n)