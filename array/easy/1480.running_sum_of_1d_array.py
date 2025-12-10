"""
Problem Number: 1480. Running Sum of 1d Array
Difficulty Level: Easy
Link: https://leetcode.com/problems/running-sum-of-1d-array

********************************************************************************

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

from typing import List


# Solution 1: With additional data structure
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        cum_sum = 0
        for i in range(n):
            cum_sum += nums[i]
            result[i] = cum_sum
        return result

# Time complexity: O(2 * n) ==> O(n)
# Space complexity: O(n)


# Solution 2: In-place modification
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

# Time complexity: O(n)
# Space complexity: O(n)
