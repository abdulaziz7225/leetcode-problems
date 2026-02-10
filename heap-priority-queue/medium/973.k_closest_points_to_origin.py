"""
Problem Number: 973. K Closest Points to Origin
Difficulty Level: Medium
Link: https://leetcode.com/problems/k-closest-points-to-origin

********************************************************************************

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
and an integer k, return the k closest points to the origin (0, 0). The distance between
two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except
for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
1 <= k <= points.length <= 10^4
-10^4 <= xi, yi <= 10^4
"""

from typing import List
from heapq import heappop, heappush, nsmallest


# Solution 1: Heap Priority Queue
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []

        for x, y in points:
            distance = -(x**2 + y**2)
            heappush(min_heap, (distance, x, y))
            if len(min_heap) > k:
                heappop(min_heap)

        for _, x, y in min_heap:
            result.append([x, y])

        return result

# Time Complexity: O(n * log(k) + k * log(k)) ==> O(n * log(k))
# Space Complexity: O(2 * k) ==> O(k)


# Solution 2: Built-in Quickselect Algorithm
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)

# In Python, heapq.nsmallest uses a specific hybrid strategy depending on the size of
# K relative to N. It builds a Max-Heap of the first K elements. For the remaining N - K
# elements, it compares the current element to the heap's largest (top). If the new
# element is smaller, it performs a heapreplace
# Time Complexity: O(n * log(k) + k * log(k)) ==> O(n * log(k))
# Space Complexity: O(2 * k) ==> O(k)

# TODO: Solution 3: Custom Quickselect Algorithm
