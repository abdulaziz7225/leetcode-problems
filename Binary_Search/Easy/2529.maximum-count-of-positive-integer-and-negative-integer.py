"""
Problem Number: 2529. Maximum Count of Positive Integer and Negative Integer
Difficulty Level: Easy
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer

********************************************************************************

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.
  
Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
  
Constraints:
1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
  Follow up: Can you solve the problem in O(log(n)) time complexity?
"""

from typing import List


# Solution 1
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_occurrence_of_zero = self.binary_search(nums, 0, True)
        last_occurrence_of_zero = self.binary_search(nums, 0, False)
        return max(first_occurrence_of_zero, len(nums) - last_occurrence_of_zero)

    def binary_search(self, nums, target, searching_left):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if searching_left:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] > 0:
                right = middle - 1
            else:
                left = middle + 1
                
        return left

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 2
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_occurrence_of_zero = self.bisect_left(nums, 0)
        first_occurrence_of_one = self.bisect_left(nums, 1)
        return max(first_occurrence_of_zero, len(nums) - first_occurrence_of_one)

    def bisect_left(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return left

# Time Complexity: O(log(n))
# Space Complexity: O(1)
