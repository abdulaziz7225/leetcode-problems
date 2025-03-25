"""
Problem Number: 56. Merge Intervals
Difficulty Level: Medium
https://leetcode.com/problems/merge-intervals

********************************************************************************

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
  
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
  
Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:
            if start > result[-1][1]:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)

        return result

# Time Complexity: O(n * log(n)) + O(n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)
