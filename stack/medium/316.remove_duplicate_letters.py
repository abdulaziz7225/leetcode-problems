"""
Problem Number: 316. Remove Duplicate Letters
Difficulty Level: Medium
Link: https://leetcode.com/problems/remove-duplicate-letters/

********************************************************************************

Given a string s, remove duplicate letters so that every letter appears once and only
once. You must make sure your result is the smallest in lexicographical order among all
possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
1 <= s.length <= 10^4
s consists of lowercase English letters.
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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
