"""
Problem Number: 547. Number of Provinces
Difficulty Level: Medium
Link: https://leetcode.com/problems/number-of-provinces

********************************************************************************

There are n cities. Some of them are connected, while some are not. If city a is
connected directly with city b, and city b is connected directly with city c, then city
a is connected indirectly with city c. A province is a group of directly or indirectly
connected cities and no other cities outside of the group. You are given an n x n matrix
isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise. Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

from collections import deque
from typing import List


# Solution 1: Iterative DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.size = len(isConnected)
        self.visited = [False] * self.size
        provinces = 0

        for i in range(self.size):
            if not self.visited[i]:
                provinces += 1
                self.dfs(i, isConnected)

        return provinces

    def dfs(self, starting_node: int, isConnected: List[List[int]]) -> None:
        stack = [starting_node]
        self.visited[starting_node] = True

        while stack:
            curr = stack.pop()

            for neighbor in range(self.size):
                if isConnected[curr][neighbor] == 1 and not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    stack.append(neighbor)

# Time Complexity: O(n^2)
# Space Complexity: O(n)


# Solution 2: Iterative BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.size = len(isConnected)
        self.visited = [False] * self.size
        provinces = 0

        for i in range(self.size):
            if not self.visited[i]:
                provinces += 1
                self.bfs(i, isConnected)

        return provinces

    def bfs(self, starting_node: int, isConnected: List[List[int]]) -> None:
        queue = deque([starting_node])
        self.visited[starting_node] = True

        while queue:
            curr = queue.popleft()

            for neighbor in range(self.size):
                if isConnected[curr][neighbor] == 1 and not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    queue.append(neighbor)

# Time Complexity: O(n^2)
# Space Complexity: O(n)
