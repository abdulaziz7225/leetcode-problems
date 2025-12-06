"""
Problem Number: 1399. Count Largest Group
Difficulty Level: Easy
https://leetcode.com/problems/count-largest-group

********************************************************************************

You are given an integer n.
Each number from 1 to n is grouped according to the sum of its digits.
Return the number of groups that have the largest size.
  
Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
  
Constraints:
1 <= n <= 10^4
"""

from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        hash_map = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = 0
            while i > 0:
                i, r = divmod(i, 10)
                digit_sum += r
            hash_map[digit_sum] += 1

        result = 0
        largest_size = max(hash_map.values())
        for value in hash_map.values():
            if value == largest_size:
                result += 1

        return result

# Time Complexity: O(n * log10(n) + 2 * log10(n)) ==> O(n * log(n))
# Space Complexity: O(log10(n)) ==> O(log(n))
