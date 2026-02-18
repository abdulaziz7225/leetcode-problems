"""
Problem Number: 621. Task Scheduler
Difficulty Level: Medium
Link: https://leetcode.com/problems/task-scheduler

********************************************************************************

You are given an array of CPU tasks, each labeled with a letter from A to Z, and
a number n. Each CPU interval can be idle or allow the completion of one task.
Tasks can be completed in any order, but there's a constraint: there has to be a
gap of at least n intervals between two tasks with the same label. Return the
minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The
same applies to task B. In the 3rd interval, neither A nor B can be done, so you
idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle ->
idle -> A -> B. There are only two types of tasks, A and B, which need to be
separated by 3 intervals. This leads to idling twice between repetitions of
these tasks.

Constraints:
1 <= tasks.length <= 10^4
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""

from typing import List
from heapq import heappush, heappop
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = dict()
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        max_heap = []
        for freq in count.values():
            heappush(max_heap, -freq)

        time = 0
        queue = deque()

        while max_heap or queue:
            time += 1

            if max_heap:
                curr_freq = heappop(max_heap) + 1

                if curr_freq < 0:
                    queue.append((curr_freq, time + n))

            if queue and queue[0][1] == time:
                heappush(max_heap, queue.popleft()[0])

        return time

# m = len(tasks), k = number of unique characters
# Time Complexity: O(m + n * m) ==> O(n * m)
# Space Complexity: O(3 * k) ==> O(k)