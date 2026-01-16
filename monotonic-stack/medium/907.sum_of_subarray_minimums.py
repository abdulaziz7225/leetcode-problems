"""
Problem Number: 907. Sum of Subarray Minimums
Difficulty Level: Medium
Link: https://leetcode.com/problems/sum-of-subarray-minimums

********************************************************************************

Given an array of integers arr, find the sum of min(b), where b ranges over every
(contiguous) subarray of arr. Since the answer may be large, return the answer modulo
109 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Constraints:
1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
"""

from typing import List

# Solution 1: Brute Force
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        modulo = 10**9 + 7
        result = 0

        for i in range(n):
            curr = arr[i]
            for j in range(i, n):
                curr = min(curr, arr[j])
                result = (result + curr) % modulo
            
        return result

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Solution 2: Monotonic Stack
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        result = [0] * len(arr)
        modulo = 10**9 + 7

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1] if stack else -1
            result[i] = result[j] + (i - j) * arr[i]

            stack.append(i)

        return sum(result) % modulo

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(n)
