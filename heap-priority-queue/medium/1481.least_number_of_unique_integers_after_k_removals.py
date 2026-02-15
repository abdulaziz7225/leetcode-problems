"""
Problem Number: 1481. Least Number of Unique Integers after K Removals
Difficulty Level: Medium
Link: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

********************************************************************************

Given an array of integers arr and an integer k. Find the least number of unique
integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""

from typing import List
from heapq import heapify, heappop


# Solution 1: Sorting
class Solution:
    def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        frequencies = sorted(count.values(), reverse=True)

        while k > 0 and frequencies[-1] <= k:
            freq = frequencies.pop()
            k -= freq

        return len(frequencies)

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + m + 2 * m * log(m)) ==> O(n + m * log(m))
# Space Complexity: O(2 * m) ==> O(m)


# Solution 2: Min Heap
class Solution:
    def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        frequencies = list(count.values())
        heapify(frequencies)

        while k > 0 and frequencies[0] <= k:
            freq = heappop(frequencies)
            k -= freq

        return len(frequencies)

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + 2 * m + m * log(m)) ==> O(n + m * log(m))
# Space Complexity: O(2 * m) ==> O(m)


# Solution 3: Counting Sort
class Solution:
    def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        n = len(nums)

        count_of_frequencies = [0] * (n + 1)
        for freq in count.values():
            count_of_frequencies[freq] += 1

        remaining_unique_elements = len(count)
        for index in range(1, n + 1):
            num_of_elements = min(k // index, count_of_frequencies[index])
            k -= index * (num_of_elements)

            remaining_unique_elements -= num_of_elements

            if k < index:
                return remaining_unique_elements

        return 0

# n = len(nums), m = count of unique numbers
# Time Complexity: O(3 * n + m) ==> O(n)
# Space Complexity: O(n + m) ==> O(n)
