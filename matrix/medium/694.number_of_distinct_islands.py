"""
Problem Number: 694. Number of Distinct Islands
Difficulty Level: Medium
Link: https://leetcode.com/problems/number-of-distinct-islands

********************************************************************************


Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may assume
all four edges of the grid are surrounded by water. Count the number of distinct
islands. An island is considered to be the same as another if and only if one island can
be translated (and not rotated or reflected) to equal the other.


Example 1:
Input: matrix = [
[11000],
[11000],
[00011],
[00011]
]
Output: 1

Example 2:
Input: matrix = [
[11011],
[10000],
[00001],
[11011]
]
Output: 3

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
"""

from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.unique_islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)

        return len(self.unique_islands)

    def dfs(self, grid: List[List[int]], i: int, j: int) -> None:
        stack = [(i, j)]
        grid[i][j] = 0

        shape = [(0, 0)]
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while stack:
            row, col = stack.pop()

            for dr, dc in directions:
                r, c = row + dr, col + dc

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    stack.append((r, c))
                    grid[r][c] = 0
                    shape.append((r - i, c - j))

        self.unique_islands.add(tuple(shape))

# m = row size of matrix, n = column size of matrix
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
