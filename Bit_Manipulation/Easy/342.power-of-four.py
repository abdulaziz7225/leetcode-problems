"""
Problem Number: 342. Power of Four
Difficulty Level: Easy
https://leetcode.com/problems/power-of-four

********************************************************************************

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
  
Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true
  
Constraints:
-2^31 <= n <= 2^31 - 1
Follow up: Could you solve it without loops/recursion?
"""


# Solution 1

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False

        binary = bin(n)[2:]
        index = len(binary) - 1
        flag = False

        for bit in binary:
            if bit == "1":
                if index % 2 == 1:
                    return False
                elif index % 2 == 0:
                    if flag:
                        return False
                    flag = True
            index -= 1
        return flag
    
# k = log(n), k = length of binary form of n
# Time Complexity: O(k)
# Space Complexity: O(1)


# Solution 2

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1 and n.bit_length() % 2 == 1

# k = log(n), k = length of binary form of n
# Time Complexity: O(k)
# Space Complexity: O(1)
