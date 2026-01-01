"""
Problem Number: 61. Rotate List
Difficulty Level: Medium
Link: https://leetcode.com/problems/rotate-list

********************************************************************************

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 1
        dummy = head
        while dummy.next:
            dummy = dummy.next
            length += 1

        k %= length
        if length < 2 or k == 0:
            return head

        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        dummy.next = head

        return new_head

# Time Complexity: O(n)
# Space Complexity: O(1)
