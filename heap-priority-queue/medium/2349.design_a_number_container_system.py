"""
Problem Number: 2349. Design a Number Container System
Difficulty Level: Medium
https://leetcode.com/problems/design-a-number-container-system

********************************************************************************

Design a number container system that can do the following:
Insert or Replace a number at the given index in the system.
Return the smallest index for the given number in the system.
Implement the NumberContainers class:
NumberContainers() Initializes the number container system.
void change(int index, int number) Fills the container at index with the number. If
there is already a number at that index, replace it.
int find(int number) Returns the smallest index for the given number, or -1 if there is
no index that is filled by number in the system.
  
Example 1:
Input
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
Output
[null, -1, null, null, null, null, 1, null, 2]

Explanation
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index
that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that
index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is
filled with 10 is 2. Therefore, we return 2.
  
Constraints:
1 <= index, number <= 10^9
At most 10^5 calls will be made in total to change and find.
"""

from heapq import heappop, heappush
from collections import defaultdict
from sortedcontainers import SortedSet


# Solution 1
class NumberContainers:

    def __init__(self):
        self.all_indices = defaultdict(SortedSet)
        self.idx_to_num = {}

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            prev_num = self.idx_to_num[index]
            self.all_indices[prev_num].discard(index)

            if len(self.all_indices[prev_num]) == 0:
                del self.all_indices[prev_num]

        self.all_indices[number].add(index)
        self.idx_to_num[index] = number

    def find(self, number: int) -> int:
        if number not in self.all_indices:
            return -1

        return self.all_indices[number][0]

# Time Complexity:
# change() method: O(log(n))
# find() method: O(1)
# Space Complexity: O(n)


# Solution 2
class NumberContainers:

    def __init__(self):
        self.num_to_indices = defaultdict(list)
        self.idx_to_num = {}

    def change(self, index: int, number: int) -> None:
        self.idx_to_num[index] = number
        heappush(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        if not self.num_to_indices[number]:
            return -1

        while self.num_to_indices[number]:
            idx = self.num_to_indices[number][0]
            if self.idx_to_num.get(idx) == number:
                return idx
            heappop(self.num_to_indices[number])

        return -1

# Time Complexity:
# change() method: O(log(n))
# k is the number of stale indices
# find() method: O(k * log(n))
# Space Complexity: O(n)
