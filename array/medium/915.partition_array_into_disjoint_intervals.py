"""
Problem Number: 915. Partition Array into Disjoint Intervals
Difficulty Level: Medium
https://leetcode.com/problems/partition-array-into-disjoint-intervals

********************************************************************************

Given an integer array nums, partition it into two (contiguous) subarrays left and right
so that: Every element in left is less than or equal to every element in right. left and
right are non-empty. left has the smallest possible size. Return the length of left
after such a partitioning. Test cases are generated such that partitioning exists.
  
Example 1:
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
  
Constraints:
2 <= nums.length <= 10^5
0 <= nums[i] <= 10^6
There is at least one valid answer for the given input.
"""

from typing import List


# Solution 1: Using one array for right min values
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        right_min_array = [0] * len(nums)
        curr_right_min = float('inf')

        for idx in range(n - 1, -1, -1):
            curr_right_min = min(curr_right_min, nums[idx])
            right_min_array[idx] = curr_right_min

        left_max = nums[0]
        for idx in range(1, n):
            if left_max <= right_min_array[idx]:
                return idx
            left_max = max(left_max, nums[idx])

        return -1

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(n)


# Solution 2: No arrays
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = nums[0]
        global_max = nums[0]
        length = 1

        for idx in range(1, len(nums)):
            if nums[idx] < curr_max:
                curr_max = global_max
                length = idx + 1
            else:
                global_max = max(global_max, nums[idx])

        return length

# Time Complexity: O(n)
# Space Complexity: O(1)
