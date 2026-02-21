"""
Problem Number: 378. Kth Smallest Element in a Sorted Matrix
Difficulty Level: Medium
Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

********************************************************************************

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix. Note that it is the kth smallest element
in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th
smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

Follow up:
Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced
for an interview but you may find reading this paper fun.
"""

from typing import List
from heapq import heappush, heappop


# Solution 1: Min Heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])

        min_heap = []
        for rowID in range(n):
            heappush(min_heap, (matrix[rowID][0], rowID, 0))

        while k > 1:
            _, rowID, colID = heappop(min_heap)
            colID += 1

            if colID < m:
                heappush(min_heap, (matrix[rowID][colID], rowID, colID))

            k -= 1

        return min_heap[0][0]

# n = len(rows), m = len(cols)
# Time Complexity: O(n + k * log(n)) ==> O(k * log(n))
# Space Complexity: O(n)


# Solution 2: Binary Search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])

        left = matrix[0][0]
        right = matrix[n - 1][m - 1]

        while left < right:
            middle = (left + right) // 2
            count = self.countLessOrEqual(matrix, n, m, middle)
            if count < k:
                left = middle + 1
            else:
                right = middle

        # return right
        return left

    def countLessOrEqual(self, matrix: List[List[int]], n: int, m: int, target: int) -> int:
        rowID = n - 1
        colID = 0
        count = 0

        while rowID >= 0 and colID < m:
            if matrix[rowID][colID] <= target:
                count += (rowID + 1)
                colID += 1
            else:
                rowID -= 1

        return count

# n = len(rows), m = len(cols), d = maximum element - minimum element
# Time Complexity: O((n + m) * log(d))
# Space Complexity: O(1)
