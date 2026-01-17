"""
Problem Number: 200. Number of Islands
Difficulty Level: Medium
Link: https://leetcode.com/problems/number-of-islands

********************************************************************************

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's
(water), return the number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically. You may assume all four edges of
the grid are all surrounded by water.

Example 1:
Input: grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import List


# Solution 1: Recursive Depth-First Search with in-place modification
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    self.dfs(grid, i, j)

        return number_of_islands

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"

        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)


# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)


# Solution 2: Iterative Depth-First Search with set data structure
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        self.visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    number_of_islands += 1
                    self.dfs(grid, i, j)

        return number_of_islands

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        stack = []
        self.visited.add((i, j))
        stack.append((i, j))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while stack:
            row, col = stack.pop()

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and \
                        grid[r][c] == "1" and (r, c) not in self.visited:
                    stack.append((r, c))
                    self.visited.add((r, c))

# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)


# Solution 3: Iterative Depth-First Search with in-place modification
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    self.dfs(grid, i, j)

        return number_of_islands

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        stack = []
        grid[i][j] = "0"
        stack.append((i, j))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while stack:
            row, col = stack.pop()

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                    grid[r][c] = "0"
                    stack.append((r, c))

# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)


# Solution 4: Iterative Breadth-First Search with set data structure
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        self.visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    number_of_islands += 1
                    self.bfs(grid, i, j)

        return number_of_islands

    def bfs(self, grid: List[List[str]], i: int, j: int) -> None:
        queue = deque()
        self.visited.add((i, j))
        queue.append((i, j))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                r, c = row + dr, col + dc

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and \
                        grid[r][c] == "1" and (r, c) not in self.visited:
                    queue.append((r, c))
                    self.visited.add((r, c))

# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)


# Solution 5: Iterative Breadth-First Search with in-place modification
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    self.bfs(grid, i, j)

        return number_of_islands

    def bfs(self, grid: List[List[str]], i: int, j: int) -> None:
        queue = deque()
        grid[i][j] = "0"
        queue.append((i, j))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                    grid[r][c] = "0"
                    queue.append((r, c))

# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)
