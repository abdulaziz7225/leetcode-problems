"""
Problem Number: 2401. Longest Nice Subarray
Difficulty Level: Medium
https://leetcode.com/problems/longest-nice-subarray

********************************************************************************

You are given an array nums consisting of positive integers.
We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
Return the length of the longest nice subarray.
A subarray is a contiguous part of an array.
Note that subarrays of length 1 are always considered nice.
  
Example 1:
Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.

Example 2:
Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
  
Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # XOR(a, b) = (a | b) - (a & b)
        # IF (a & b) == 0, THEN XOR(a, b) = (a | b)

        left = 0
        current_subarray = 0
        longest_subarray = 0

        for right in range(len(nums)):
            while current_subarray & nums[right] != 0:
                current_subarray ^= nums[left]
                left += 1

            current_subarray ^= nums[right]
            longest_subarray = max(longest_subarray, right - left + 1)

        return longest_subarray

# Time Complexity: O(n)
# Space Complexity: O(1)
