"""
Problem Number: 34. Find First and Last Position of Element in Sorted Array
Difficulty Level: Medium
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

********************************************************************************

Given an array of integers nums sorted in non-decreasing order, find the starting and
ending position of a given target value. If target is not found in the array, return
[-1, -1]. You must write an algorithm with O(log n) runtime complexity.
  
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


# Solution 1: Bisect left and bisect right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = self.firstPosition(nums, target)
        last = self.lastPosition(nums, target)
        return [first, last]

    def firstPosition(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        return left if nums[left] == target else -1

    def lastPosition(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right + 1) // 2
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle

        return right if nums[right] == target else -1


# Time Complexity: O(log(n))
# Space Complexity: O(1)

# Solution 2: Two bisect left calls
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = self.bisect_left(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = self.bisect_left(nums, target + 1) - 1
        return [first, last]

    def bisect_left(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        return left

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 3: Search towards a specific direction
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.custom_binary_search(nums, target, True)
        last = self.custom_binary_search(nums, target, False)
        return [first, last]

    def custom_binary_search(self, nums: List[int], target: int, is_searching_first: bool) -> int:
        left = 0
        right = len(nums) - 1
        index = -1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                index = middle
                if is_searching_first:
                    right = middle - 1
                else:
                    left = middle + 1

        return index

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 4: Binary Search Template III
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = self.custom_binary_search(nums, target, True)
        last = self.custom_binary_search(nums, target, False)
        return [first, last]

    def custom_binary_search(self, nums: List[int], target: int, is_searching_first: bool) -> int:
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            middle = (left + right) // 2

            if (nums[middle] > target) or (is_searching_first and nums[middle] == target):
                right = middle
            else:
                left = middle

        if is_searching_first:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
        else:
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left

        return -1

# Time Complexity: O(log(n))
# Space Complexity: O(1)
