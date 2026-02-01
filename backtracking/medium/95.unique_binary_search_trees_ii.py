"""
Problem Number: 95. Unique Binary Search Trees II
Difficulty Level: Medium
Link: https://leetcode.com/problems/unique-binary-search-trees-ii

********************************************************************************

Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 8
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Recursive Dynamic Programming without hashmap
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = dict()
        return self.allPossibleBST(1, n)

    def allPossibleBST(self, start: int, end: int):
        result = []

        if start > end:
            result.append(None)
            return result

        if (start, end) in self.memo:
            return self.memo[(start, end)]

        for root_val in range(start, end + 1):
            left_subtrees = self.allPossibleBST(start, root_val - 1)
            right_subtrees = self.allPossibleBST(root_val + 1, end)

            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(root_val, left, right)
                    result.append(root)

        self.memo[(start, end)] = result
        return result

# Time Complexity: O(4^n / sqrt(n))
# Space Complexity: O(4^n / sqrt(n))


# Solution 2: Recursive Dynamic Programming with hashmap
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = dict()
        return self.allPossibleBST(1, n)

    def allPossibleBST(self, start: int, end: int):
        result = []

        if start > end:
            result.append(None)
            return result

        if start == end:
            node = TreeNode(start)
            result.append(node)
            return result

        for root_val in range(start, end + 1):
            left_subtrees = self.allPossibleBST(start, root_val - 1)
            right_subtrees = self.allPossibleBST(root_val + 1, end)

            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(root_val, left, right)
                    result.append(root)

        return result

# Time Complexity: O(4^n / sqrt(n))
# Space Complexity: sum((n - k + 1) * 4^k / sqrt(k)) when k is from 1 to n
