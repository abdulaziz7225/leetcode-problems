"""
Problem Number: 448. Find All Numbers Disappeared in an Array
Difficulty Level: Easy
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

********************************************************************************

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

from typing import List


# Solution 1: Cyclic Sort
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        result = []

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result

# k = count of disappeared numbers
# Time Complexity: O(3 * n - 1)
# Space Complexity: O(k)
