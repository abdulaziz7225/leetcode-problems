"""
Problem Number: 28. Find the Index of the First Occurrence in a String
Difficulty Level: Easy
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

********************************************************************************

Given two strings needle and haystack, return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.
  
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
  
Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""


# Solution 1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        idx = 0
        curr = 0

        while idx < haystack_len:
            if haystack[idx] == needle[curr]:
                curr += 1
            else:
                idx -= curr
                curr = 0

            if curr == needle_len:
                return idx - (needle_len - 1)
            idx += 1
        return -1

# n = len(haystack), m = len(needle)
# Time Complexity: O(n * m)
# Space Complexity: O(1)


# Solution 2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1

# n = len(haystack), m = len(needle)
# Time Complexity: O(n * m)
# Space Complexity: O(m)


# Solution 3
# TODO: Solve the problem using the Knuth-Morris-Pratt (KMP) and Rabin-Karp Algorithms
