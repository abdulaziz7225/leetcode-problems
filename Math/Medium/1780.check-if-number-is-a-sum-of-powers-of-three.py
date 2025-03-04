"""
Problem Number: 1780. Check if Number is a Sum of Powers of Three
Difficulty Level: Medium
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three

********************************************************************************

Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
An integer y is a power of three if there exists an integer x such that y == 3x.
  
Example 1:
Input: n = 12
Output: true
Explanation: 12 = 31 + 32

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34

Example 3:
Input: n = 21
Output: false
  
Constraints:
1 <= n <= 10^7
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            n, r = divmod(n, 3)
            if r == 2:
                return False
        return True

# Time Complexity: O(log3(n))
# Space Complexity: O(1)
