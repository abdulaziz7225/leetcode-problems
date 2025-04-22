"""
Problem Number: 3467. Transform Array by Parity
Difficulty Level: Easy
https://leetcode.com/problems/transform-array-by-parity

********************************************************************************

You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:
Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.
  
Example 1:
Input: nums = [4,3,2,1]
Output: [0,0,1,1]
Explanation:
Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
After sorting nums in non-descending order, nums = [0, 0, 1, 1].

Example 2:
Input: nums = [1,5,1,4,2]
Output: [0,0,1,1,1]
Explanation:
Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, nums = [1, 1, 1, 0, 0].
After sorting nums in non-descending order, nums = [0, 0, 1, 1, 1].
  
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 1000
"""

from typing import List


# Solution 1
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even, odd = 0, 0
        for num in nums:
            if num & 1 == 0:
                even += 1
            else:
                odd += 1
        return [0] * even + [1] * odd

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 2
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            nums[i] = nums[i] & 1
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)
