"""
Problem Number: 3334. Apple Redistribution into Boxes
Difficulty Level: Easy
Link: https://leetcode.com/problems/apple-redistribution-into-boxes

********************************************************************************

You are given an array apple of size n and an array capacity of size m.
There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.
Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
Note that, apples from the same pack can be distributed into different boxes.

Example 1:
Input: apple = [1,3,2], capacity = [4,3,1,5,2]
Output: 2
Explanation: We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.

Example 2:
Input: apple = [5,5,5], capacity = [2,4,2,7]
Output: 4
Explanation: We will need to use all the boxes.

Constraints:
1 <= n == apple.length <= 50
1 <= m == capacity.length <= 50
1 <= apple[i], capacity[i] <= 50
The input is generated such that it's possible to redistribute packs of apples into boxes.
"""
from typing import List
from heapq import _heapify_max, _heappop_max


# Solution 1: Sorting
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        count = 0

        while total_apples > 0 and count < len(capacity):
            total_apples -= capacity[count]
            count += 1

        return count

# n = len(apple), m = len(capacity)
# Time complexity: O(n + m + m * log(m)) ==> O(n + m * log(m))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space complexity: O(m)


# Solution 2: Heap Priority Queue
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        _heapify_max(capacity)
        count = 0

        while total_apples > 0:
            total_apples -= _heappop_max(capacity)
            count += 1

        return count

# n = len(apple), m = len(capacity)
# Time complexity: O(n + m + m * log(m)) ==> O(n + m * log(m))
# Space complexity: O(1)
