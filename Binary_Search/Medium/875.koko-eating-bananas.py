"""
Problem Number: 875. Koko Eating Bananas
Difficulty Level: Medium
https://leetcode.com/problems/koko-eating-bananas

********************************************************************************

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
  
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
  
Constraints:
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""

from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            middle = (left + right) // 2

            total_hours = sum(ceil(pile / middle) for pile in piles)

            if total_hours <= h:
                result = middle
                right = middle - 1
            else:
                left = middle + 1 

        return result

# N = len(piles), M = max(piles)
# Time Complexity: O(N * log(M))
# Space Complexity: O(1)
