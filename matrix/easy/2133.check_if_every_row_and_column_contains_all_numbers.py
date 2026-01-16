"""
Problem Number: 2133. Check if Every Row and Column Contains All Numbers
Difficulty Level: Easy
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers

********************************************************************************

An n x n matrix is valid if every row and every column contains all the integers from 1
to n (inclusive). Given an n x n integer matrix matrix, return true if the matrix is
valid. Otherwise, return false.
  
Example 1:
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

Example 2:
Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain
the numbers 2 or 3. Hence, we return false.
  
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n
"""

from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            row_set = set()
            col_set = set()
            for j in range(n):
                row_set.add(matrix[i][j])
                col_set.add(matrix[j][i])
            if len(row_set) != n or len(col_set) != n:
                return False
        return True

# Time Complexity: O(n^2)
# Space Complexity: O(n)
