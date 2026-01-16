"""
Problem Number: 1752. Check if Array Is Sorted and Rotated
Difficulty Level: Easy
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

********************************************************************************

Given an array nums, return true if the array was originally sorted in non-decreasing
order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array. Note: An array A rotated by x positions
results in an array B of the same length such that A[i] == B[(i+x) % A.length], where %
is the modulo operation.
  
Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3:
[3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
  
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from typing import List


# Solution 1
class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                x = i
                break

        if x != 0:
            for i in range(x, len(nums)):
                if nums[i] < nums[x] or nums[i] > nums[0]:
                    return False 
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 2
class Solution:
    def check(self, nums: List[int]) -> bool:
        x = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                x += 1
                if x > 1:
                    return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)
