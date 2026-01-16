"""
Problem Number: 367. Valid Perfect Square
Difficulty Level: Easy
https://leetcode.com/problems/valid-perfect-square

********************************************************************************

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is
the product of some integer with itself. You must not use any built-in library function,
such as sqrt.
  
Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
  
Constraints:
1 <= num <= 2^31 - 1
"""


# Solution 1: Math Trick
# Valid Perfect Square is equal to sum of odd numbers sum(1+3+5+ ... +(2n-1))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd_number = 1
        while num > 0:
            num -= odd_number
            odd_number += 2
        return num == 0

# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)


# Solution 2: Binary Search
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        while left <= right:
            middle = (left + right) // 2
            if middle ** 2 == num:
                return True
            elif middle ** 2 < num:
                left = middle + 1
            else:
                right = middle - 1
        return False

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 3: Newton's method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r ** 2 > num:
            r = (r + num / r) // 2
        return r ** 2 == num

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 4: Bit Manipulation
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = 0
        bit = 1 << 15
        while bit > 0:
            root |= bit
            if root > num // root:
                root ^= bit
            bit >>= 1
        return root ** 2 == num

# Time Complexity: O(log(n))
# Space Complexity: O(1)
