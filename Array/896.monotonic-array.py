"""
Problem Number: 896. Monotonic Array
Difficulty Level: Easy
https://leetcode.com/problems/monotonic-array

********************************************************************************

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for 
all i <= j, nums[i] >= nums[j]. Given an integer array nums, return true if the given array is monotonic, or false otherwise.
  
Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false
  
Constraints:
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
"""

from typing import List


# Solution 1: Using Two Flags
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_inc = is_dec = True

        for i in range(1, len(nums)):
            if not is_inc and not is_dec:
                return False

            if nums[i-1] > nums[i]:
                is_inc = False
            if nums[i-1] < nums[i]:
                is_dec = False

        return is_inc or is_dec
    
# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 2: Using a Single Flag
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc_or_dec = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if inc_or_dec == -1: # -1 for decreasing array
                    return False
                inc_or_dec = 1

            if nums[i - 1] > nums[i]:
                if inc_or_dec == 1: # 1 for increasing array
                    return False
                inc_or_dec = -1
                
        return True
    
# Time Complexity: O(n)
# Space Complexity: O(1)
