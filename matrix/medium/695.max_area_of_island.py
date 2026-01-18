"""
Problem Number: 695. Max Area of Island
Difficulty Level: Medium
Link: https://leetcode.com/problems/max-area-of-island/

********************************************************************************

You are given an m x n binary matrix grid. An island is a group of 1's (representing
land) connected 4-directionally (horizontal or vertical.) You may assume all four edges
of the grid are surrounded by water. The area of an island is the number of cells with a
value 1 in the island. Return the maximum area of an island in grid. If there is no
island, return 0.

Example 1:
Input: grid = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

from collections import deque
from typing import List


# Solution 1: Iterative Depth-First Search with in-place modification
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = self.dfs(grid, i, j)
                    max_area = max(max_area, curr_area)

        return max_area

    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        curr_area = 1
        stack = [(i, j)]
        grid[i][j] = 0

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while stack:
            row, col = stack.pop()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    curr_area += 1
                    grid[r][c] = 0
                    stack.append((r, c))

        return curr_area

# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)


# Solution 2: Iterative Breadth-First Search with in-place modification
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = self.bfs(grid, i, j)
                    max_area = max(max_area, curr_area)

        return max_area

    def bfs(self, grid: List[List[int]], i: int, j: int) -> int:
        curr_area = 1
        queue = deque()
        queue.append((i, j))
        grid[i][j] = 0

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    curr_area += 1
                    grid[r][c] = 0
                    queue.append((r, c))

        return curr_area

# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)
