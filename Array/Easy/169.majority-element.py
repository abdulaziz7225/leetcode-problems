"""
Problem Number: 169. Majority Element
Difficulty Level: Easy
https://leetcode.com/problems/majority-element

********************************************************************************

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
  
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
  
Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        counter = 0
        for num in nums:
            if counter == 0:
                majority = num
                counter = 1
            elif num == majority:
                counter += 1
            else:
                counter -= 1
        return majority


# Boyer–Moore majority vote algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
