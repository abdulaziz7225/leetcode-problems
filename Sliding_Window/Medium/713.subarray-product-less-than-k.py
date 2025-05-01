"""
Problem Number: 713. Subarray Product Less Than K
Difficulty Level: Medium
https://leetcode.com/problems/subarray-product-less-than-k

********************************************************************************

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
  
Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0
  
Constraints:
1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count, left = 0, 0
        cum_prod = 1

        for right in range(len(nums)):
            cum_prod *= nums[right]

            while left <= right and cum_prod >= k:
                cum_prod //= nums[left]
                left += 1
            count += right - left + 1

        return count

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(1)
