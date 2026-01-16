"""
Problem Number: 287. Find the Duplicate Number
Difficulty Level: Medium
Link: https://leetcode.com/problems/find-the-duplicate-number

********************************************************************************

Given an array of integers nums containing n + 1 integers where each integer is in the
range [1, n] inclusive. There is only one repeated number in nums, return this repeated
number. You must solve the problem without modifying the array nums and using only
constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

from typing import List


# Solution 1: Cyclic Sort
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]

        return n

# Time Complexity: O(3 * n - 1) ==> O(n)
# Space Complexity: O(1)


# Solution 2: Fast and Slow Pointers
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

# Time Complexity: O(3 * n - 1) ==> O(n)
# Space Complexity: O(1)
