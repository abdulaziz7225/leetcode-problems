"""
Problem Number: 231. Power of Two
Difficulty Level: Easy
https://leetcode.com/problems/power-of-two

********************************************************************************

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
  
Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
  
Constraints:
-2^31 <= n <= 2^31 - 1
  Follow up: Could you solve it without loops/recursion?
"""


# Solution 1: Iterative approach
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        curr = 1
        while curr < n:
            curr *= 2
        return curr == n

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 2: Bit Manipulation
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 8 (1000) & 7 (0111) == 0 ✅
        # 5 (0101) & 4 (0100) != 0 ❌
        return n > 0 and (n & (n - 1)) == 0

# Time Complexity: O(1)
# Space Complexity: O(1)
