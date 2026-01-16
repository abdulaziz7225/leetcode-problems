"""
Problem Number: 16. 3Sum Closest
Difficulty Level: Medium
Link: https://leetcode.com/problems/3sum-closest

********************************************************************************

Given an integer array nums of length n and an integer target, find three integers in
nums such that the sum is closest to target. Return the sum of the three integers. You
may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        result = float("inf")

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == target:
                    return total
                elif abs(total - target) < abs(result - target):
                    result = total
                elif total < target:
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result

# Time Complexity: O(n * log(n) + n^2) ==> O(n^2)
# In Python, the sort() method sorts a list using the Timsort algorithm and has O(n) additional space.
# Space Complexity: O(n)
