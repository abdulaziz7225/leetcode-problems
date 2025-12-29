"""
Problem Number: 986. Interval List Intersections
Difficulty Level: Medium
https://leetcode.com/problems/interval-list-intersections

********************************************************************************

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
  
Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
  
Constraints:
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= start[i] < end[i] <= 10^9
end[i] < start[i]+1
0 <= start[j] < end[j] <= 10^9 
end[j] < start[j]+1
"""

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1, ptr2 = 0, 0
        result = []

        while ptr1 < len(firstList) and ptr2 < len(secondList):
            a_start, a_end = firstList[ptr1]
            b_start, b_end = secondList[ptr2]

            if a_start <= b_end and b_start <= a_end:
                result.append([max(a_start, b_start), min(a_end, b_end)])

            if a_end <= b_end:
                ptr1 += 1
            else:
                ptr2 += 1

        return result

# n = len(firstList), m = len(secondList)
# Time Complexity: O(n + m)
# Space Complexity: O(1)
