"""
Problem Number: 560. Subarray Sum Equals K
Difficulty Level: Medium
https://leetcode.com/problems/subarray-sum-equals-k

********************************************************************************

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
  
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
  
Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        diff_sum = {0: 1}
        cum_sum = 0
        result = 0

        for num in nums:
            cum_sum += num
            if cum_sum - k in diff_sum:
                result += diff_sum[cum_sum - k]

            diff_sum[cum_sum] = diff_sum.get(cum_sum, 0) + 1

        return result
    
# Time Complexity: O(n)
# Space Complexity: O(n)
