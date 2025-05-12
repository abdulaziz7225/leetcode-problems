"""
Problem Number: 75. Sort Colors
Difficulty Level: Medium
https://leetcode.com/problems/sort-colors

********************************************************************************

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
  
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
  
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
  Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

from typing import List


# Solution 1: Two-pass Approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow = 0

        for fast in range(n):
            if nums[fast] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

        for fast in range(slow, n):
            if nums[fast] == 1:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(1)


# Solution 2: Dutch national flag problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

# Time Complexity: O(n)
# Space Complexity: O(1)
