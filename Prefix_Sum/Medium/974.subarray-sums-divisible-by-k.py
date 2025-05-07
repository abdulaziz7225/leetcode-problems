"""
Problem Number: 974. Subarray Sums Divisible by K
Difficulty Level: Medium
https://leetcode.com/problems/subarray-sums-divisible-by-k

********************************************************************************

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.
  
Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0
  
Constraints:
1 <= nums.length <= 3 * 10^4
-104 <= nums[i] <= 10^4
2 <= k <= 10^4
"""

from typing import List


# Solution 1
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = {0: 1}
        count, cum_sum = 0, 0

        for num in nums:
            cum_sum += num
            cum_sum %= k
            remainder[cum_sum] = remainder.get(cum_sum, 0) + 1

        for freq in remainder.values():
            count += freq * (freq - 1) // 2

        return count

# Time Complexity: O(n + k)
# Space Complexity: O(k)


# Solution 2
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count, cum_sum = 0, 0
        remainder = [0] * k
        remainder[0] = 1

        for num in nums:
            cum_sum += num
            cum_sum %= k
            count += remainder[cum_sum]
            remainder[cum_sum] += 1

        return count

# Time Complexity: O(n + k)
# Space Complexity: O(k)
