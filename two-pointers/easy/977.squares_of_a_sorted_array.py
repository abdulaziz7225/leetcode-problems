"""
Problem Number: 977. Squares of a Sorted Array
Difficulty Level: Easy
https://leetcode.com/problems/squares-of-a-sorted-array

********************************************************************************

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
  
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
  
Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
  Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) >= abs(nums[right]):
                result[idx] = nums[left] ** 2
                left += 1
            else:
                result[idx] = nums[right] ** 2
                right -= 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
