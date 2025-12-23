"""
Problem Number: 844. Backspace String Compare
Difficulty Level: Easy
Link: https://leetcode.com/problems/backspace-string-compare

********************************************************************************

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ptr1 = len(s) - 1
        ptr2 = len(t) - 1

        while ptr1 >= 0 or ptr2 >= 0:
            ptr1 = self.getNextValidIndex(s, ptr1)
            ptr2 = self.getNextValidIndex(t, ptr2)

            if ptr1 >= 0 and ptr2 >= 0 and s[ptr1] != t[ptr2]:
                return False

            if (ptr1 >= 0) ^ (ptr2 >= 0):
                return False

            ptr1 -= 1
            ptr2 -= 1

        return True

    def getNextValidIndex(self, string: str, index: int) -> int:
        backspace_count = 0

        while index >= 0:
            if string[index] == "#":
                backspace_count += 1
            elif string[index] != "#" and backspace_count > 0:
                backspace_count -= 1
            else:
                break
            index -= 1

        return index

# n = len(s), m = len(t)
# Time Complexity: O(n + m)
# Space Complexity: O(1)
