"""
Problem Number: 1763. Longest Nice Substring
Difficulty Level: Easy
Link: https://leetcode.com/problems/longest-nice-substring

********************************************************************************

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

Example 1:
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

Constraints:
1 <= s.length <= 100
s consists of uppercase and lowercase English letters.
"""


# Solution 1: Divide and Conquer
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        char_set = set(s)

        for idx, char in enumerate(s):
            if char.swapcase() in char_set:
                continue

            left_subarray = self.longestNiceSubstring(s[:idx])
            right_subarray = self.longestNiceSubstring(s[idx + 1:])
            return max(left_subarray, right_subarray, key=len)

        return s

# Time Complexity:
# Average Case: O(n * log(n))
# Worst Case: O(n^2)
# Space Complexity: O(n^2)


# Solution 2: Improved Divide and Conquer
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        char_set = set(s)

        bad_chars = set()
        for char in char_set:
            if char.swapcase() not in char_set:
                bad_chars.add(char)

        if not bad_chars:
            return s

        s_list = []
        for char in s:
            if char in bad_chars:
                s_list.append(" ")
            else:
                s_list.append(char)
        s = "".join(s_list)

        subarrays = s.split(" ")

        longest_nice_subarray = ""
        for subarray in subarrays:
            candidate = self.longestNiceSubstring(subarray)
            if len(candidate) > len(longest_nice_subarray):
                longest_nice_subarray = candidate

        return longest_nice_subarray

# n = len(s), k = 26 (number of lowercase English letters)
# Time Complexity: O(n * k) ==> O(n)
# Space Complexity: O(n * k) ==> O(n)


# Solution 3: Improved Divide and Conquer
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        self.s = s
        self.final_start = 0
        self.final_len = 0

        self.divide_and_conquer(0, len(s))
        return self.s[self.final_start: self.final_start + self.final_len]

    def divide_and_conquer(self, start: int, end: int) -> None:
        if end - start <= self.final_len:
            return

        current_set = set()
        for idx in range(start, end):
            current_set.add(self.s[idx])

        bad_chars = set()
        for char in current_set:
            if char.swapcase() not in current_set:
                bad_chars.add(char)

        if not bad_chars:
            self.final_len = end - start
            self.final_start = start
            return

        prev = start
        for idx in range(start, end):
            if self.s[idx] in bad_chars:
                self.divide_and_conquer(prev, idx)
                prev = idx + 1

        self.divide_and_conquer(prev, end)

# n = len(s), k = 26 (number of lowercase English letters)
# Time Complexity: O(n * k) ==> O(n)
# Space Complexity: O(k) ==> O(1)
