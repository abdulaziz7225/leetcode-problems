"""
Problem Number: 209. Minimum Size Subarray Sum
Difficulty Level: Medium
https://leetcode.com/problems/minimum-size-subarray-sum

********************************************************************************

Given an array of positive integers nums and a positive integer target, return the
minimal length of a subarray whose sum is greater than or equal to target. If there is
no such subarray, return 0 instead.
  
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
  
Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
  Follow up: If you have figured out the O(n) solution, try coding another solution of
  which the time complexity is O(n * log(n)).
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_window = 0
        min_window = float("inf")

        for right in range(len(nums)):
            curr_window += nums[right]

            while left <= right and curr_window >= target:
                min_window = min(min_window, right - left + 1)
                curr_window -= nums[left]
                left += 1

        if min_window == float("inf"):
            return 0
        return min_window

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(1)
