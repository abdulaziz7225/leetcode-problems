"""
Problem Number: 515. Find Largest Value in Each Tree Row
Difficulty Level: Medium
Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row

********************************************************************************

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-2^31 <= Node.val <= 2^31 - 1
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        result = []

        queue.append(root)

        while queue:
            level_size = len(queue)
            curr_max = float("-inf")

            for _ in range(level_size):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(curr_max)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
