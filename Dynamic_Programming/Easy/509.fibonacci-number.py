"""
Problem Number: 509. Fibonacci Number
Difficulty Level: Easy
https://leetcode.com/problems/fibonacci-number

********************************************************************************

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
  
Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
  
Constraints:
0 <= n <= 30
"""


# Solution 1: Tabulation approach with storing
class Solution:
    def fib(self, n: int) -> int:
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            fib_seq.append(fib_seq[-2] + fib_seq[-1])
        return fib_seq[n]

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 2: Tabulation approach without storing
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 3: Memoization(Top-Down) approach
class Solution:
    hash_map = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.hash_map:
            return self.hash_map[n]

        self.hash_map[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.hash_map[n]

# Time Complexity: O(n)
# Space Complexity: O(n)
