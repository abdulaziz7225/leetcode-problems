"""
Problem Number: 74. Search a 2D Matrix
Difficulty Level: Medium
Link: https://leetcode.com/problems/search-a-2d-matrix

********************************************************************************

You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""

from typing import List


# Solution 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top < bottom:
            middle_row_idx = (top + bottom + 1) // 2
            row_start_value = matrix[middle_row_idx][0]

            if row_start_value == target:
                return True
            elif row_start_value < target:
                top = middle_row_idx
            else:
                bottom = middle_row_idx - 1

        left = 0
        right = len(matrix[0]) - 1
        target_row = matrix[bottom]

        while left <= right:
            middle_col_idx = (left + right) // 2
            col_start_value = matrix[target_row][middle_col_idx]

            if col_start_value == target:
                return True
            elif col_start_value < target:
                left = middle_col_idx + 1
            else:
                right = middle_col_idx - 1

        return False

# Time Complexity: O(log(n) + log(m)) ==> O(log(n * m))
# Space Complexity: O(1)


# Solution 2: One-Pass or Virtual Array Approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            middle = (left + right) // 2
            row_idx, col_idx = divmod(middle, cols)
            guess = matrix[row_idx][col_idx]

            if guess == target:
                return True
            elif guess < target:
                left = middle + 1
            else:
                right = middle - 1

        return False

# Time Complexity: O(log(n) + log(m)) ==> O(log(n * m))
# Space Complexity: O(1)
