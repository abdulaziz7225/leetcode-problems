"""
Problem Number: 96. Unique Binary Search Trees
Difficulty Level: Medium
Link: https://leetcode.com/problems/unique-binary-search-trees

********************************************************************************

Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 19
"""


class Solution:
    def numTrees(self, n: int) -> int:
        uniq_trees = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += uniq_trees[root - 1] * uniq_trees[nodes - root]
            uniq_trees[nodes] = total

        return uniq_trees[n]

# Time Complexity: O(n^2)
# Space Complexity: O(n)
