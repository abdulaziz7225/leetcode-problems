"""
Problem Number: 709. To Lower Case
Difficulty Level: Easy
https://leetcode.com/problems/to-lower-case

********************************************************************************

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
  
Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"
  
Constraints:
1 <= s.length <= 100
s consists of printable ASCII characters.
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for char in s:
            curr = char
            if 65 <= ord(char) <= 90:
                curr = chr(ord(char) + 32)
            result.append(curr)
        return "".join(result)

# Time Complexity: O(n)
# Space Complexity: O(n)
