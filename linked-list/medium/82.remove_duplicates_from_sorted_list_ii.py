"""
Problem Number: 82. Remove Duplicates from Sorted List II
Difficulty Level: Medium
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

********************************************************************************

Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as
well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional["ListNode"] = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next is curr:
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)
