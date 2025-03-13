"""
Problem Number: 3356. Zero Array Transformation II
Difficulty Level: Medium
https://leetcode.com/problems/zero-array-transformation-ii

********************************************************************************

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
Each queries[i] represents the following action on nums:
Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.
Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.
  
Example 1:
Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
Output: 2
Explanation:
For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:
Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
Output: -1
Explanation:
For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.
  
Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 5 * 10^5
1 <= queries.length <= 10^5
queries[i].length == 3
0 <= li <= ri < nums.length
1 <= vali <= 5
"""

from typing import List


# Solution 1: Binary Search
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left = 0
        right = len(queries) - 1

        if not self.zero_array(nums, queries, right + 1):
            return -1

        while left <= right:
            middle = (left + right) // 2
            if self.zero_array(nums, queries, middle):
                right = middle - 1
                result = middle
            else:
                left = middle + 1

        return left

    def zero_array(self, nums: List[int], queries: List[List[int]], k: int) -> bool:
        n = len(nums)

        diff_array = [0] * (n + 1)
        for left, right, value in queries[:k]:
            diff_array[left] -= value
            diff_array[right + 1] += value

        curr_sum = 0
        for i in range(n):
            curr_sum += diff_array[i]
            if curr_sum + nums[i] > 0:
                return False
        return True

# N = len(nums), M = len(queries)
# Time Complexity: O((N + M) * log(M))
# Space Complexity: O(N)


# Solution 2: Line Sweep Approach
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        k = 0
        curr_sum = 0
        diff_array = [0] * (n + 1)

        for idx in range(n):

            while curr_sum + diff_array[idx] + nums[idx] > 0:
                if k == len(queries):
                    return -1

                left, right, value = queries[k]

                if right >= idx:
                    diff_array[max(left, idx)] -= value
                    diff_array[right + 1] += value
                k += 1

            curr_sum += diff_array[idx]

        return k

# N = len(nums), M = len(queries)
# Time Complexity: O(N + M)
# Space Complexity: O(N)
