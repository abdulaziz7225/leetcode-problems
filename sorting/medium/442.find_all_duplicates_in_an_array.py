"""
Problem Number: 442. Find All Duplicates in an Array
Difficulty Level: Medium
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array

********************************************************************************

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""

from typing import List


# Solution 1: Cyclic Sort
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        duplicates = list()

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates

# k = count of duplicate numbers
# Time Complexity: O(3 * n - 1)
# Space Complexity: O(k)
