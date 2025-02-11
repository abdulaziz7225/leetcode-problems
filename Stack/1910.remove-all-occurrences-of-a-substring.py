"""
Problem Number: 1910. Remove All Occurrences of a Substring
Difficulty Level: Medium
https://leetcode.com/problems/remove-all-occurrences-of-a-substring

********************************************************************************

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.
A substring is a contiguous sequence of characters in a string.
  
Example 1:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

Example 2:
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
  
Constraints:
1 <= s.length <= 1000
1 <= part.length <= 1000
s and part consists of lowercase English letters.
"""


# Solution 1
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        len_of_part = len(part)
        for char in s:
            stack.append(char)

            if len(stack) >= len_of_part and \
            self.check_match(stack, part, len_of_part):
                for _ in range(len_of_part):
                    stack.pop()

        return "".join(stack)

    def check_match(self, stack, part, len_of_part):
        return "".join(stack[-len_of_part:]) == part
    
#  n = len(s), m = len(part)
# Time Complexity: O(n * m)
# Space Complexity: O(n + m)


# Solution 2
# TODO: Solve the problem using the Knuth-Morris-Pratt (KMP) Algorithm