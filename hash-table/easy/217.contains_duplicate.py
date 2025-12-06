"""
Problem Number: 217. Contains Duplicate
Difficulty Level: Easy
https://leetcode.com/problems/contains-duplicate

********************************************************************************

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
  
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
  
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
