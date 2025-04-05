"""
Problem Number: 1854. Maximum Population Year
Difficulty Level: Easy
https://leetcode.com/problems/maximum-population-year

********************************************************************************

You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.
Return the earliest year with the maximum population.
  
Example 1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

Example 2:
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation: 
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.
  
Constraints:
1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050
"""

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        diff_sum = [0] * 101

        for birth, death in logs:
            diff_sum[birth - 1950] += 1
            diff_sum[death - 1950] -= 1

        max_alive = 0
        earliest_year = 0
        curr_diff = 0

        for idx, year in enumerate(diff_sum):
            curr_diff += year
            if curr_diff > max_alive:
                max_alive = curr_diff
                earliest_year = idx + 1950

        return earliest_year

# Time Complexity: O(n + 101) ==> O(n)
# Space Complexity: O(101) ==> O(1)
