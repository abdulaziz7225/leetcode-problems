"""
Problem Number: 257. Binary Tree Paths
Difficulty Level: Easy
Link: https://leetcode.com/problems/binary-tree-paths

********************************************************************************

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths = []
        self.dfs(root, [], all_paths)
        return all_paths

    def dfs(self, root: Optional[TreeNode], path: List[str], all_paths: List[List[int]]) -> None:
        if not root:
            return None

        path.append(str(root.val))

        if not root.left and not root.right:
            all_paths.append("->".join(path))
        else:
            self.dfs(root.left, path, all_paths)
            self.dfs(root.right, path, all_paths)

        path.pop()

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
