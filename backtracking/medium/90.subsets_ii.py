"""
Problem Number: 90. Subsets II
Difficulty Level: Medium
Link: https://leetcode.com/problems/subsets-ii/

********************************************************************************

Given an integer array nums that may contain duplicates, return all possible subsets
(the power set). The solution set must not contain duplicate subsets. Return the
solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

from typing import List


# Solution 1
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = [[]]
        i = 0

        while i < n:
            count = 0
            while i + count < n and nums[i] == nums[i + count]:
                count += 1

            previous_count = len(result)
            for k in range(previous_count):
                subset = result[k].copy()

                for _ in range(count):
                    subset.append(nums[i])
                    result.append(subset.copy())
            i += count

        return result

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)


# Solution 2
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = [[]]

        end_index = 0
        for i in range(n):
            start_index = 0

            if i > 0 and nums[i - 1] == nums[i]:
                start_index = end_index

            end_index = len(result)
            for k in range(start_index, end_index):
                subset = result[k].copy()
                subset.append(nums[i])
                result.append(subset)

        return result

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
