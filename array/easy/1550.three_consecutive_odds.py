"""
Problem Number: 1550. Three Consecutive Odds
Difficulty Level: Easy
https://leetcode.com/problems/three-consecutive-odds

********************************************************************************

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
  
Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
  
Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num & 1 == 1:
                count += 1
            else:
                count = 0

            if count == 3:
                return True
        return False

# Time Complexity: O(n)
# Space Complexity: O(1)
