"""
Problem Number: 404. Sum of Left Leaves
Difficulty Level: Easy
https://leetcode.com/problems/sum-of-left-leaves

********************************************************************************

Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
  
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0
  
Constraints:
The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, is_left_child=False)

    def helper(self, node, is_left_child):
        if node:
            if is_left_child and not node.left and not node.right:
                return node.val
            return self.helper(node.left, True) + self.helper(node.right, False)
        return 0

# Time Complexity: O(n)
# Space Complexity: O(n) - worst case, O(log(n)) - best case for a balanced tree


# Solution 2
# TODO: Solve the problem using iterative approach