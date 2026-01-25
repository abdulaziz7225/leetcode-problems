"""
Problem Number: 436. Find Right Interval
Difficulty Level: Medium
Link: https://leetcode.com/problems/find-right-interval

********************************************************************************

You are given an array of intervals, where intervals[i] = [starti, endi] and each starti
is unique. The right interval for an interval i is an interval j such that startj >=
endi and startj is minimized. Note that i may equal j. Return an array of right interval
indices for each interval i. If no right interval exists for interval i, then put -1 at
index i.

Example 1:
Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

Example 3:
Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.

Constraints:
1 <= intervals.length <= 2 * 10^4
intervals[i].length == 2
-10^6 <= starti <= endi <= 10^6
The start point of each interval is unique.
"""

from typing import List
from heapq import heappush, heappop


# Solution 1: Binary Search Approach
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        self.starts = sorted([(interval[0], idx)
                             for idx, interval in enumerate(intervals)])

        result = []
        for _, end in intervals:
            right_interval = self.custom_binary_search(intervals, end)

            if right_interval < n:
                result.append(self.starts[right_interval][1])
            else:
                result.append(-1)

        return result

    def custom_binary_search(self, intervals: List[List[int]], end: int) -> int:
        left = 0
        right = len(intervals)

        while left < right:
            middle = (left + right) // 2
            if self.starts[middle][0] >= end:
                right = middle
            else:
                left = middle + 1

        return left

# Time Complexity: O(2 * n * log(n)) ==> O(n * log(n))
# Space Complexity: O(3 * n) ==> O(n)


# Solution 2: Two Heaps Approach
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        max_start = []
        max_end = []

        result = [-1] * n

        for idx, (start, end) in enumerate(intervals):
            heappush(max_start, (-start, idx))
            heappush(max_end, (-end, idx))

        for _ in range(n):
            end, idx = heappop(max_end)

            if -max_start[0][0] >= -end:
                start, index = heappop(max_start)

                while max_start and -max_start[0][0] >= -end:
                    start, index = heappop(max_start)

                result[idx] = index
                heappush(max_start, (start, index))

        return result

# Time Complexity: O(4 * n * log(n)) ==> O(n * log(n))
# Space Complexity: O(3 * n) ==> O(n)
