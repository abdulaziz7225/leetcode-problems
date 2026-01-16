"""
Problem Number: 73. Set Matrix Zeroes
Difficulty Level: Medium
https://leetcode.com/problems/set-matrix-zeroes

********************************************************************************

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column
to 0's. You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
  Follow up:
A straightforward solution using O(m*n) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

from typing import List


# Solution 1: Using additional O(n * m) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vertical, horizontal = set(), set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    vertical.add(row)
                    horizontal.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in vertical or col in horizontal:
                    matrix[row][col] = 0

# n = row size of matrix, m = column size of matrix
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n + m)


# Solution 2: Using O(1) space and two flags
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_col_has_zero = True
                    if col == 0:
                        first_row_has_zero = True
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, row_len):
            for col in range(1, col_len):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_col_has_zero:
            for col in range(col_len):
                matrix[0][col] = 0

        if first_row_has_zero:
            for row in range(row_len):
                matrix[row][0] = 0

# n = row size of matrix, m = column size of matrix
# Time Complexity: O(2 * n * m + n + m) ==> O(n * m)
# Space Complexity: O(1)


# Solution 3: Using O(1) space and single flag
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        first_col = False

        for row in range(row_len):
            if matrix[row][0] == 0:
                first_col = True
            for col in range(1, col_len):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(row_len - 1, -1, -1):
            for col in range(1, col_len):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if first_col:
                matrix[row][0] = 0

# n = row size of matrix, m = column size of matrix
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n + m)
