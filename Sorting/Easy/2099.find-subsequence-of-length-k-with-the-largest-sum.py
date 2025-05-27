"""
Problem Number: 2099. Find Subsequence of Length K With the Largest Sum
Difficulty Level: Easy
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum

********************************************************************************

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
Return any such subsequence as an integer array of length k.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
  
Example 1:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.

Example 2:
Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

Example 3:
Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
  
Constraints:
1 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

from typing import List
from heapq import heappush, heappushpop


# Solution 1: Using min-heap (size k)
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        largest_k = []

        for idx, num in enumerate(nums):
            if len(largest_k) == k:
                heappushpop(largest_k, (num, idx))
            else:
                heappush(largest_k, (num, idx))

        sorted_by_index = sorted(largest_k, key=lambda x: x[1])
        return [num for num, _ in sorted_by_index]

# Time Complexity: O(n * log(k) + k * log(k)) ==> O((n + k) * log(k))
# Space Complexity: O(2 * k) => O(k)


# Solution 2: Sorting
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(idx, num) for idx, num in enumerate(nums)]
        indexed_nums.sort(key = lambda x: x[1], reverse = True)

        top_k_pairs = sorted(indexed_nums[:k])

        return [num for _, num in top_k_pairs]
    
# Time Complexity: O(n * (log(n) + 1) + k * (log(k) + 1)) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2* n + 2 * k) => O(n + k)
