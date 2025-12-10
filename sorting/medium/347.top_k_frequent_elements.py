"""
Problem Number: 347. Top K Frequent Elements
Difficulty Level: Medium
Link: https://leetcode.com/problems/top-k-frequent-elements

********************************************************************************

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:
1 <= nums.length <= 10^5
-104 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from heapq import nlargest
from typing import List


# Solution 1: Sorting
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        top_frequent = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(top_frequent[i][0])
        return result

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + m * log(m) + k) ==> O(n + m * log(m))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * m + k) ==> O(m)


# Solution 2: Heap Priority Queue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = nlargest(k, count.keys(), key=count.get)
        return result

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + m * log(m) + k) ==> O(n + m * log(m))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * m + k) ==> O(m)
