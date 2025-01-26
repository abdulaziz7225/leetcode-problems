"""
Problem Number: 144. Binary Tree Preorder Traversal
Difficulty Level: Easy
https://leetcode.com/problems/binary-tree-preorder-traversal

********************************************************************************

Given the root of a binary tree, return the preorder traversal of its nodes' values.
  
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
Explanation:

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]
Explanation:

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]
  
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node:
            result.append(node.val)
            self.helper(node.left, result)
            self.helper(node.right, result)

# The time complexity is O(n) because the recursive function is T(n)=2⋅T(n/2)+1.
# Space complexity: O(n). The worst case space required is O(n), and in the average case it's O(logn) where n is number of nodes.


# Solution 2
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            curr = curr.right
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)