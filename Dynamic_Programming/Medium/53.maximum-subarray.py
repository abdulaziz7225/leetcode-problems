"""
Problem Number: 53. Maximum Subarray
Difficulty Level: Medium
https://leetcode.com/problems/maximum-subarray

********************************************************************************

Given an integer array nums, find the subarray with the largest sum, and return its sum.
  
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
  
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
  Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            largest_sum = max(largest_sum, curr_sum)
        return largest_sum

# Time Complexity: O(n)
# Space Complexity: O(1)

# TODO: Solve this problem using Dynamic Programming - Memoization and Tabulation

# TODO: Solve this problem using Divide & Conquer
