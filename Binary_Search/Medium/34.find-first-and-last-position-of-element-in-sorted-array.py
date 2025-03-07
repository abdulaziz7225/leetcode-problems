"""
Problem Number: 34. Find First and Last Position of Element in Sorted Array
Difficulty Level: Medium
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

********************************************************************************

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
  
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
  
Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""

from typing import List


# Solution 1
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]

        first_idx = self.bisect_left(nums, target)
        if first_idx == len(nums) or nums[first_idx] != target:
            return [-1, -1]

        last_idx = self.bisect_left(nums, target + 1, first_idx) - 1
        return [first_idx, last_idx]

    def bisect_left(self, array, target, low=0):
        high = len(array) - 1
        while low <= high:
            middle = (low + high) // 2
            if array[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return low

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 2
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_position = self.binary_search(nums, target, True)
        last_position = self.binary_search(nums, target, False)

        return [first_position, last_position]
    
    def binary_search(self, arr, target, is_searching_left):
        left = 0
        right = len(arr) - 1
        idx = -1

        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == target:
                idx = middle
                if is_searching_left:
                    right = middle - 1
                else:
                    left = middle + 1
            elif arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return idx

# Time Complexity: O(log(n))
# Space Complexity: O(1)
