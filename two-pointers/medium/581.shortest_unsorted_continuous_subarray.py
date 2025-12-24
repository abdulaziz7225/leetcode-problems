"""
Problem Number: 581. Shortest Unsorted Continuous Subarray
Difficulty Level: Medium
Link: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

********************************************************************************

Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0

Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5

Follow up: Can you solve it in O(n) time complexity?
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, -1
        max_val = float("-inf")
        min_val = float("inf")

        for i in range(n):
            if nums[i] >= max_val:
                max_val = nums[i]
            else:
                right = i

        for i in range(n - 1, -1, -1):
            if nums[i] <= min_val:
                min_val = nums[i]
            else:
                left = i

        return max(0, right - left + 1)

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(1)
