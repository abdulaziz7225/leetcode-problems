"""
Problem Number: 103. Binary Tree Zigzag Level Order Traversal
Difficulty Level: Medium
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

********************************************************************************

Given the root of a binary tree, return the zigzag level order traversal of its nodes'
values. (i.e., from left to right, then right to left for the next level and alternate
between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        result = []

        queue.append(root)
        left_to_right = True

        while queue:
            level_size = len(queue)
            curr_level = deque()

            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    curr_level.append(node.val)
                else:
                    curr_level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            left_to_right = not left_to_right
            result.append(list(curr_level))

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
