"""
Problem Number: 1081. Smallest Subsequence of Distinct Characters
Difficulty Level: Medium
Link: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters

********************************************************************************

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index = dict()
        for index, char in enumerate(s):
            last_index[char] = index

        visited = set()
        stack = []
        for index, char in enumerate(s):
            if char in visited:
                continue

            while stack and stack[-1] > char and last_index[stack[-1]] > index:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return "".join(stack)

# n = len(string), c = 26
# Time complexity; O(4 * n) ==> O(n)
# Space complexity: O(3 * c) ==> O(1)
