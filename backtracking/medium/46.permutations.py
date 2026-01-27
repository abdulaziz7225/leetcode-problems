"""
Problem Number: 46. Permutations
Difficulty Level: Medium
Link: https://leetcode.com/problems/permutations

********************************************************************************

Given an array nums of distinct integers, return all the possible permutations. You can
return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List
from collections import deque


# Solution 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = deque(nums)
        return self.backtrack(queue)
    
    def backtrack(self, queue: deque) -> List[List[int]]:
        if len(queue) == 1:
            return [list(queue)]
        
        result = []

        for _ in range(len(queue)):
            curr = queue.popleft()
            permutations = self.backtrack(queue)

            for perm in permutations:
                perm.append(curr)

            result.extend(permutations)
            queue.append(curr)

        return result
    
# Time Complexity: O(n * n!)
# Space Complexity: O(n * n!)

# Solution 2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(0, nums)
        return self.result

    def backtrack(self, start: int, nums: List[int]) -> None:
        if start == len(nums):
            self.result.append(nums.copy())
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.backtrack(start + 1, nums)
            nums[start], nums[i] = nums[i], nums[start]

# Time Complexity: O(n * n!)
# Space Complexity: O(n * n!)
