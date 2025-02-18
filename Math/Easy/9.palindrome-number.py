"""
Problem Number: 9. Palindrome Number
Difficulty Level: Easy
https://leetcode.com/problems/palindrome-number

********************************************************************************

Given an integer x, return true if x is a
palindrome
, and false otherwise.
  
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
  
Constraints:
-2^31 <= x <= 2^31 - 1
  Follow up: Could you solve it without converting the integer to a string?
"""


# Solution 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_x = 0

        while x > reversed_x:
            x, remainder = divmod(x, 10)
            reversed_x = 10 * reversed_x + remainder

        return x == reversed_x or x == reversed_x // 10

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = 0
        temp = x
        while temp > 0:
            temp, remainder = divmod(temp, 10)
            reversed_x = 10 * reversed_x + remainder

        return x == reversed_x

# Time Complexity: O(log(n))
# Space Complexity: O(1)
