"""
Problem Number: 92. Reverse Linked List II
Difficulty Level: Medium
Link: https://leetcode.com/problems/reverse-linked-list-ii

********************************************************************************

Given the head of a singly linked list and two integers left and right where left <=
right, reverse the nodes of the list from position left to position right, and return
the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        
        # 1. Reach the node at position "left"
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next

        # 2. Reverse from left to right
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 2
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)

        # 1. Reach the node at position "left"
        left_prev = dummy
        curr = head
        for _ in range(left - 1):
            left_prev = curr
            curr = curr.next

        # 2. Reverse from left to right
        prev = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Update pointers
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)
