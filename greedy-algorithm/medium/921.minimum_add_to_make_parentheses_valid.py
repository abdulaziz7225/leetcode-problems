"""
Problem Number: 921. Minimum Add to Make Parentheses Valid
Difficulty Level: Medium
Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

********************************************************************************

A parentheses string is valid if and only if:
It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any
position of the string. For example, if s = "()))", you can insert an opening
parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:
Input: s = "())"
Output: 1

Example 2:
Input: s = "((("
Output: 3

Constraints:
1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""


# Solution 1: Stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if stack and stack[-1] == "(" and char == ")":
                stack.pop()
            else:
                stack.append(char)

        return len(stack)

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 2: Open Bracket Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_add_required = 0

        for char in s:
            if char == "(":
                open_brackets += 1
            elif open_brackets > 0:
                open_brackets -= 1
            else:
                min_add_required += 1

        return open_brackets + min_add_required

# Time Complexity: O(n)
# Space Complexity: O(1)
