"""
Problem Number: 747. Largest Number At Least Twice of Others
Difficulty Level: Easy
https://leetcode.com/problems/largest-number-at-least-twice-of-others

********************************************************************************

You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
  
Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
  
Constraints:
2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
"""

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_idx = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_idx]:
                max_idx = i

        for i in range(len(nums)):
            if i != max_idx and nums[max_idx] < 2 * nums[i]:
                return -1
        return max_idx

# Time Complexity: O(n)
# Space Complexity: O(1)
