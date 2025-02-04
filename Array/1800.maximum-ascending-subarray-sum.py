"""
Problem Number: 1800. Maximum Ascending Subarray Sum
Difficulty Level: Easy
https://leetcode.com/problems/maximum-ascending-subarray-sum

********************************************************************************

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.
  
Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
  
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

# Maximum Subarray Sum – Kadane’s Algorithm
from typing import List


# Solution 1
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += nums[i]
                max_sum = max(max_sum, curr)
            else:
                curr = nums[i]
        return max_sum

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 2
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                max_sum = max(max_sum, curr)
                curr = 0
            curr += nums[i]
        return max(max_sum, curr)

# Time Complexity: O(n)
# Space Complexity: O(1)
