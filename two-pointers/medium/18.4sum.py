"""
Problem Number: 18. 4Sum
Difficulty Level: Medium
Link: https://leetcode.com/problems/4sum

********************************************************************************

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""

from typing import List


# Solution 1: Extension of 3Sum problem
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append(
                            [nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result

# Time Complexity: O(n * log(n) + n^3) ==> O(n^3)
# In the worst-case scenario, the number of unique quadruplets is proportional to the cube of the input size
# Space Complexity: O(n + n^3) ==> O(n^3)


# Solution 2: Generic KSum solution
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)

    def kSum(self, array: List[int], target: int, k: int) -> List[List[int]]:
        result = []

        if not array:
            return result

        average_value = target // k
        if array[-1] < average_value < array[0]:
            return result

        if k == 2:
            return self.twoSum(array, target)

        for i in range(len(array)):
            if i > 0 and array[i - 1] == array[i]:
                continue

            for subset in self.kSum(array[i + 1:], target - array[i], k - 1):
                result.append([array[i]] + subset)

        return result

    def twoSum(self, array: List[int], target: int) -> List[List[int]]:
        pairs = []

        left = 0
        right = len(array) - 1

        while left < right:
            curr_sum = array[left] + array[right]
            if curr_sum == target:
                pairs.append([array[left], array[right]])
                left += 1
                right -= 1
                while left < right and array[left - 1] == array[left]:
                    left += 1
                while left < right and array[right] == array[right + 1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return pairs

# k = 4 for 4Sum problem
# Time Complexity: O(n * log(n) + n^(k - 1)) ==> O(n^(k - 1)) ==> O(n^3)
# Space Complexity: O(n + n^(k - 1)) ==> O(n^(k - 1)) ==> O(n^3)
