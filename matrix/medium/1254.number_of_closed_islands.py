"""
Problem Number: 1254. Number of Closed Islands
Difficulty Level: Medium
Link: https://leetcode.com/problems/number-of-closed-islands

********************************************************************************

Given a 2D grid consists of 0s (land) and 1s (water). An island is a maximal
4-directionally connected group of 0s and a closed island is an island totally (all
left, top, right, bottom) surrounded by 1s. Return the number of closed islands.

Example 1:
Input: grid = [
[1,1,1,1,1,1,1,0],
[1,0,0,0,0,1,1,0],
[1,0,1,0,1,1,1,0],
[1,0,0,0,0,1,0,1],
[1,1,1,1,1,1,1,0]
]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [
[1,1,1,1,1,1,1],
[1,0,0,0,0,0,1],
[1,0,1,1,1,0,1],
[1,0,1,0,1,0,1],
[1,0,1,1,1,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1]
]
Output: 2

Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""

from typing import List


# Solution: Iterative Depth-First Search with in-place modification
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        closed_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    closed_islands += self.dfs(grid, i, j)

        return closed_islands

    def dfs(self, grid: List[List[int]], i: int, j: int) -> bool:
        is_closed = True
        stack = [(i, j)]
        grid[i][j] = 1

        while stack:
            row, col = stack.pop()
            if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1:
                is_closed = False
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:

                    grid[r][c] = 1
                    stack.append((r, c))

        return is_closed

# n = len(rows), m = len(cols)
# Time Complexity: O(n * m)
# Space Complexity: O(1)
