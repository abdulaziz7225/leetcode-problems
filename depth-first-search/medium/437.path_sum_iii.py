"""
Problem Number: 437. Path Sum III
Difficulty Level: Medium
Link: https://leetcode.com/problems/path-sum-iii

********************************************************************************

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        self.all_paths = {0: 1}

        self.dfs(root, targetSum, 0)
        return self.result

    def dfs(self, root: Optional[TreeNode], target: int, curr_sum: int) -> bool:
        if not root:
            return

        curr_sum += root.val
        self.result += self.all_paths.get(curr_sum - target, 0)
        self.all_paths[curr_sum] = self.all_paths.get(curr_sum, 0) + 1

        self.dfs(root.left, target, curr_sum)
        self.dfs(root.right, target, curr_sum)

        self.all_paths[curr_sum] -= 1

# Time Complexity: O(n)
# Space Complexity: O(n)
