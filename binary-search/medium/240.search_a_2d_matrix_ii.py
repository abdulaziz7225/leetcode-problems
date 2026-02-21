"""
Problem Number: 240. Search a 2D Matrix II
Difficulty Level: Medium
Link: https://leetcode.com/problems/search-a-2d-matrix-ii

********************************************************************************

Write an efficient algorithm that searches for a value target in an m x n integer matrix
matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""

from typing import List


# Solution 1: Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left = 0
            right = len(row) - 1

            while left <= right:
                middle = (left + right) // 2
                if row[middle] == target:
                    return True
                elif row[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
        return False

# n = lens(rows), m = len(columns)
# Time Complexity: O(n * log(m))
# Space Complexity: O(1)


# Solution 2: Efficient Traversal
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        rowID = n - 1
        colID = 0

        while rowID >= 0 and colID < m:
            if matrix[rowID][colID] == target:
                return True
            elif matrix[rowID][colID] < target:
                colID += 1
            else:
                rowID -= 1

        return False

# n = lens(rows), m = len(columns)
# Time Complexity: O(n + m)
# Space Complexity: O(1)
