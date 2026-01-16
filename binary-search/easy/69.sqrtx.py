"""
Problem Number: 69. Sqrt(x)
Difficulty Level: Easy
https://leetcode.com/problems/sqrtx

********************************************************************************

Given a non-negative integer x, return the square root of x rounded down to the nearest
integer. The returned integer should be non-negative as well. You must not use any
built-in exponent function or operator. For example, do not use pow(x, 0.5) in c++ or x
** 0.5 in python.
  
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the
nearest integer, 2 is returned.
  
Constraints:
0 <= x <= 2^31 - 1
"""


# Solution 1: Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            middle = (left + right) // 2
            square = middle ** 2
            if square == x:
                return middle
            elif square < x:
                left = middle + 1
            else:
                right = middle - 1

        # Alternatively: return left - 1
        return right

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 2: Newton's method
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r ** 2 > x:
            r = (r ** 2 + x) // (2 * r)
        return r

# Time Complexity: O(log(n))
# Space Complexity: O(1)
