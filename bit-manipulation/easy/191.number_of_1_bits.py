"""
Problem Number: 191. Number of 1 Bits
Difficulty Level: Easy
https://leetcode.com/problems/number-of-1-bits

********************************************************************************

Given a positive integer n, write a function that returns the number of set bits in its
binary representation (also known as the Hamming weight).
  
Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
  
Constraints:
1 <= n <= 2^31 - 1
Follow up: If this function is called many times, how would you optimize it?
"""


# Solution 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
    
# Time Complexity: O(1)
# Space Complexity: O(1)


# Solution 2
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(32):
            if n >> i & 1:
                result += 1
        return result

# Time Complexity: O(1)
# Space Complexity: O(1)
