"""
Problem Number: 234. Palindrome Linked List
Difficulty Level: Easy
Link: https://leetcode.com/problems/palindrome-linked-list/

********************************************************************************

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.findMiddleElement(head)

        front = head
        back = self.reverseLinkedList(middle.next)
        middle.next = None


        while front and back:
            if front.val != back.val:
                return False

            front = front.next
            back = back.next

        return True

    def findMiddleElement(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next

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

# Time Complexity: O(3 * (n // 2)) ==> O(n)
# Space Complexity: O(1)
