"""
Problem Number: 48. Rotate Image
Difficulty Level: Easy
https://leetcode.com/problems/rotate-image/

********************************************************************************

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        
        # Flip the matrix upside down.
        for row in range(n//2):
            mat[row], mat[n - row - 1] = mat[n - row - 1], mat[row]

        # Transpose the matrix
        for row in range(n):
            for col in range(row + 1, n):
                mat[row][col], mat[col][row] = mat[col][row], mat[row][col]

# Time Complexity: O(n^2)
# Space Complexity: O(1)
