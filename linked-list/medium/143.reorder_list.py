"""
Problem Number: 143. Reorder List
Difficulty Level: Medium
Link: https://leetcode.com/problems/reorder-list/

********************************************************************************

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        middle = self.findMiddleElement(head)

        front = head
        back = self.reverseLinkedList(middle.next)
        middle.next = None

        while front and back:
            ptr1 = front.next
            ptr2 = back.next

            front.next = back
            back.next = ptr1

            front = ptr1
            back = ptr2

    def findMiddleElement(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

# Time Complexity: O(3 * (n // 2) ==> O(n)
# Space Complexity: O(1)
