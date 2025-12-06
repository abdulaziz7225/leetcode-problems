"""
Problem Number: 326. Power of Three
Difficulty Level: Easy
https://leetcode.com/problems/power-of-three

********************************************************************************

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
  
Example 1:
Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
  
Constraints:
-2^31 <= n <= 2^31 - 1
  Follow up: Could you solve it without loops/recursion?
"""


# Solution 1
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n > 1:
            n, r = divmod(n, 3)
            if r != 0:
                return False
        return True

# Time Complexity: O(log3(n))
# Space Complexity: O(1)


# Solution 2
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0

# Time Complexity: O(1)
# Space Complexity: O(1)
