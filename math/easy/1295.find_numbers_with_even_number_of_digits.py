"""
Problem Number: 1295. Find Numbers with Even Number of Digits
Difficulty Level: Easy
https://leetcode.com/problems/find-numbers-with-even-number-of-digits

********************************************************************************

Given an array nums of integers, return how many of them contain an even number of digits.
  
Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
  
Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""

from typing import List


# Solution 1: Digit Counting
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            digit_count = 0
            while num > 0:
                num //= 10
                digit_count += 1

            if digit_count & 1 == 0:
                result += 1

        return result

# n = len(nums), m = maximum integer in the given array
# Time Complexity: O(n * log10(m)) ==> O(n * log(m))
# Space Complexity: O(1)


# Solution 2: Constraint Anaylsis
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            if (num >= 10 and num < 100) or (num >= 1000 and num < 10000) \
                    or (num == 100000):
                result += 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(1)
