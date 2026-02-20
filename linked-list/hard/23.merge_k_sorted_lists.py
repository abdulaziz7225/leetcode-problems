"""
Problem Number: 23. Merge k Sorted Lists
Difficulty Level: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists

********************************************************************************

You are given an array of k linked-lists lists, each linked-list is sorted in ascending
order. Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
1->4->5,
1->3->4,
2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""

from typing import List, Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Heap Priority Queue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for index, node in enumerate(lists):
            if not node:
                continue
            heappush(min_heap, (node.val, index, node))

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            _, index, node = heappop(min_heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heappush(min_heap, (node.next.val, index, node.next))

        return dummy.next

# n = total count of numbers, k = number of linked lists
# Time Complexity: O(k * log(k) + (n - k) * log(k)) ==> O(n * log(k))
# Space Complexity: O(k)


# Solution 2: Merge two linked lists at a time
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for index in range(0, len(lists), 2):
                list1 = lists[index]
                list2 = lists[index + 1] if index + 1 < len(lists) else None
                merged_lists.append(self.mergeTwoSortedLists(list1, list2))

            lists = merged_lists

        return lists[0]

    def mergeTwoSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next

# n = total count of numbers, k = number of linked lists
# Time Complexity: O(n * log(k))
# Space Complexity: O(k)
