"""
Problem Number: 124. Binary Tree Maximum Path Sum
Difficulty Level: Hard
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum

********************************************************************************

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the
sequence has an edge connecting them. A node can only appear in the sequence at most
once. Note that the path does not need to pass through the root. The path sum of a path
is the sum of the node's values in the path. Given the root of a binary tree, return the
maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.dfs(root)
        return self.result

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_sum = max(0, self.dfs(root.left))
        right_sum = max(0, self.dfs(root.right))

        self.result = max(self.result, root.val + left_sum + right_sum)
        return root.val + max(left_sum, right_sum)

# Time Complexity: O(n)
# Space Complexity: O(n)
