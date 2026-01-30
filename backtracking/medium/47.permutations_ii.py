"""
Problem Number: 47. Permutations II
Difficulty Level: Medium
Link: https://leetcode.com/problems/permutations-ii

********************************************************************************

Given a collection of numbers, nums, that might contain duplicates, return all possible
unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
[1,2,1],
[2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.counter = dict()
        for num in nums:
            self.counter[num] = self.counter.get(num, 0) + 1

        self.backtrack(nums, [])
        return self.result

    def backtrack(self, nums: List[int], perm: List[int]) -> None:
        if len(perm) == len(nums):
            self.result.append(perm.copy())
            return

        for num in self.counter:
            if self.counter[num] < 1:
                continue

            perm.append(num)
            self.counter[num] -= 1

            self.backtrack(nums, perm)

            perm.pop()
            self.counter[num] += 1

# Time Complexity: O(n * n!)
# Space Complexity: O(n * n! + 3 * n) ==> O(n * n!)
