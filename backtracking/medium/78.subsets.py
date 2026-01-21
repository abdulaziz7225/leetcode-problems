"""
Problem Number: 78. Subsets
Difficulty Level: Medium
Link: https://leetcode.com/problems/subsets

********************************************************************************

Given an integer array nums of unique elements, return all possible subsets (the power
set). The solution set must not contain duplicate subsets. Return the solution in any
order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

from typing import List


# Solution 1: Iterative approach
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            new_subset = []

            for curr in result:
                temp = curr.copy()
                temp.append(num)
                new_subset.append(temp)

            for curr in new_subset:
                result.append(curr)

        return result

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)


# Solution 2: Backtracking approach
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.result

    def backtrack(self, first: int, curr: List[int], nums: List[int]) -> None:
        self.result.append(curr.copy())
        for i in range(first, self.n):
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n + n) ==> O(n * 2^n)


# Solution 3: Lexicographic (Binary Sorted) Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]

            subset = []
            for j in range(n):
                if bitmask[j] == "1":
                    subset.append(nums[j])
            result.append(subset)

        return result

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
