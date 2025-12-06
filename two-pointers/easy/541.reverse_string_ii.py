"""
Problem Number: 541. Reverse String II
Difficulty Level: Easy
https://leetcode.com/problems/reverse-string-ii

********************************************************************************

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
  
Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
  
Constraints:
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^4
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        flag = 0
        index = 0
        result = []

        while index < len(s):
            if flag & 1 == 0:
                temp = self.reverse_array(list(s[index:index + k]))
                result.extend(temp)
            else:
                result.extend(s[index:index + k])
            flag += 1
            index += k

        return "".join(result)

    def reverse_array(self, arr):
        left, right = 0, len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr

# Time Complexity: O(n)
# Space Complexity: O(n)
