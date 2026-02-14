"""
Problem Number: 658. Find K Closest Elements
Difficulty Level: Medium
Link: https://leetcode.com/problems/find-k-closest-elements

********************************************************************************

Given a sorted integer array arr, two integers k and x, return the k closest integers to
x in the array. The result should also be sorted in ascending order. An integer a is
closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
"""

from typing import List
from heapq import heappush, heappop


# Solution 1: Heap Priority Queue
class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in nums:
            heappush(max_heap, (-abs(num - x), -num))
            if len(max_heap) > k:
                heappop(max_heap)

        result = []
        for _, num in max_heap:
            result.append(-num)

        result.sort()
        return result

# n = len(nums)
# Time Complexity: O((n + k) * log(k) + k) ==> O((n + k) * log(k))
# Space Complexity: O(2 * k) ==> O(k)


# Solution 2: Binary Search
class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(nums) - k

        while left < right:
            middle = (left + right) // 2
            if x - nums[middle] > nums[middle + k] - x:
                left = middle + 1
            else:
                right = middle

        return nums[left:left + k]

# n = len(nums)
# Time Complexity: O(log(n - k) + k) ==> O(log(n) + k)
# Space Complexity: O(k)
