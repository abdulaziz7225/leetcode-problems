"""
Problem Number: 905. Sort Array By Parity
Difficulty Level: Easy
https://leetcode.com/problems/sort-array-by-parity

********************************************************************************

Given an integer array nums, move all the even integers at the beginning of the array
followed by all the odd integers. Return any array that satisfies this condition.
  
Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
  
Constraints:
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""

from typing import List


# Solution 1
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        curr = 0
        for i in range(len(nums)):
            if nums[i] & 1 == 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                curr += 1
        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 2
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] & 1 == 0:
                left += 1
            elif nums[right] & 1 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)
