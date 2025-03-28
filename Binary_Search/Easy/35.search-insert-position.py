"""
Problem Number: 35. Search Insert Position
Difficulty Level: Easy
https://leetcode.com/problems/search-insert-position/

********************************************************************************

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_index, end_index = 0, len(nums) - 1

        while start_index <= end_index:
            mid = (end_index + start_index) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start_index = mid + 1
            else:
                end_index = mid - 1

        return start_index

# Time Complexity: O(log(n))
# Space Complexity: O(1)
