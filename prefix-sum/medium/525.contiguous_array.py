"""
Problem Number: 525. Contiguous Array
Difficulty Level: Medium
https://leetcode.com/problems/contiguous-array

********************************************************************************

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
  
Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Example 3:
Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
  
Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr_sum, result = 0, 0
        first_occurrence = {0: -1}

        for idx, num in enumerate(nums):
            if num == 1:
                curr_sum += 1
            else:
                curr_sum -= 1

            if curr_sum in first_occurrence:
                result = max(result, idx - first_occurrence[curr_sum])
            else:
                first_occurrence[curr_sum] = idx
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
