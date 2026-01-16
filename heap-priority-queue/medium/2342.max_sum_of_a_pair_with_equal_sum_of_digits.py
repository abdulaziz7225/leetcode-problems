"""
Problem Number: 2342. Max Sum of a Pair With Equal Sum of Digits
Difficulty Level: Medium
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits

********************************************************************************

You are given a 0-indexed array nums consisting of positive integers. You can choose two
indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal
to that of nums[j]. Return the maximum value of nums[i] + nums[j] that you can obtain
over all possible indices i and j that satisfy the conditions.
  
Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
  
Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

from typing import List
from collections import defaultdict
from heapq import heappush, heappop


# Solution 1
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        equal_sum = defaultdict(list)
        result = -1
        for num in nums:
            digit_sum = self.sum_of_digits(num)
            heappush(equal_sum[digit_sum], num)

            if len(equal_sum[digit_sum]) > 2:
                heappop(equal_sum[digit_sum])

        for pair_nums in equal_sum.values():
            if len(pair_nums) == 2:
                result = max(result, sum(pair_nums))
        return result
        
    def sum_of_digits(self, num):
        sum = 0
        while num > 0:
            num, remainder = divmod(num, 10)
            sum += remainder        
        return sum
    
# m is the maximum number in nums
# Time Complexity: O(n * log(m))
# Space Complexity: O(log(m))


# Solution 2
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        equal_sum = {}
        result = -1
        for num in nums:
            digit_sum = self.sum_of_digits(num)
            if digit_sum in equal_sum:
                result = max(result, equal_sum[digit_sum] + num)
                equal_sum[digit_sum] = max(equal_sum[digit_sum], num)
            else:
                equal_sum[digit_sum] = num
        return result
        
    def sum_of_digits(self, num):
        sum = 0
        while num > 0:
            num, remainder = divmod(num, 10)
            sum += remainder        
        return sum
    
# m is the maximum number in nums
# Time Complexity: O(n * log(m))
# Space Complexity: O(log(m))
