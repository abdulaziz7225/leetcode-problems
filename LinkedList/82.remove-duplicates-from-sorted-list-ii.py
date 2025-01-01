"""
Problem Number: 82. Remove Duplicates from Sorted List II
Difficulty Level: Medium
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

********************************************************************************

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well. 

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
        self.next = next
        
class Solution:
    def deleteDuplicates(self):
        prev_node = None
        curr_node = self.head
        flag = False
        while curr_node:
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
                flag = True
            elif curr_node.val != curr_node.next.val and flag is True:
                if not prev_node:
                    prev_node = curr_node.next
                    self.head = prev_node
                else:
                    prev_node.next = curr_node.next
                curr_node = curr_node.next
                flag = False
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return self.head
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.val)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
linked_list = Solution()
for elem in [1,2,3,3,4,4,5,5,5,5,5,5,5,5]:
    linked_list.append(elem)
print(linked_list)
linked_list.deleteDuplicates()
print(linked_list)
# Time Complexity: O(n)
# Space Complexity: O(1)