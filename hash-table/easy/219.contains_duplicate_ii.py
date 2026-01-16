"""
Problem Number: 219. Contains Duplicate II
Difficulty Level: Easy
Link: https://leetcode.com/problems/contains-duplicate-ii

********************************************************************************

Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique_nums = set()
        for idx, val in enumerate(nums):
            if idx > k:
                unique_nums.remove(nums[idx - k - 1])

            if nums[idx] in unique_nums:
                return True

            unique_nums.add(val)
        return False

# Time Complexity: O(n)
# Space Complexity: O(k)
