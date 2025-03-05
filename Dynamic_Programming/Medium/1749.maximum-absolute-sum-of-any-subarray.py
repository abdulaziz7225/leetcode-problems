"""
Problem Number: 1749. Maximum Absolute Sum of Any Subarray
Difficulty Level: Medium
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray

********************************************************************************

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.
Note that abs(x) is defined as follows:
If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
  
Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
  
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from typing import List


# Solution 1: Kadane’s Algorithm
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        largest_sum = float('-inf')
        curr_largest = 0
        minimum_sum = float('inf')
        curr_minimum = 0

        for num in nums:
            curr_largest = max(curr_largest + num, num)
            largest_sum = max(largest_sum, curr_largest)

            curr_minimum = min(curr_minimum + num, num)
            minimum_sum = min(minimum_sum, curr_minimum)

        return max(abs(largest_sum), abs(minimum_sum))

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 2: Prefix Sum
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_prefix_sum = 0
        min_prefix_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max_prefix_sum - min_prefix_sum

# Time Complexity: O(n)
# Space Complexity: O(1)
