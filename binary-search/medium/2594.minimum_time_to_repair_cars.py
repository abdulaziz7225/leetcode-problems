"""
Problem Number: 2594. Minimum Time to Repair Cars
Difficulty Level: Medium
https://leetcode.com/problems/minimum-time-to-repair-cars

********************************************************************************

You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.
You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.
Return the minimum time taken to repair all the cars.
Note: All the mechanics can repair the cars simultaneously.
  
Example 1:
Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation: 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.

Example 2:
Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation: 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.
  
Constraints:
1 <= ranks.length <= 10^5
1 <= ranks[i] <= 100
1 <= cars <= 10^6
"""

from typing import List
from collections import Counter
from math import sqrt


# Solution 1: Time-optimized Binary Search
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        counter = Counter(ranks)
        min_rank = min(ranks)

        left = 1
        right = min_rank * (cars ** 2)

        while left <= right:
            middle = (left + right) // 2

            total_cars_repaired = 0
            for rank, freq in counter.items():
                total_cars_repaired += freq * int(sqrt(middle / rank))

            if total_cars_repaired >= cars:
                right = middle - 1
            else:
                left = middle + 1

        return left

# n = len(ranks), m = number of cars, k = number of possible ranks
# Time Complexity: O(n * log(min_rank * m ^ 2) ==> O(n * log(min_rank * m)
# Space Complexity: O(k) for k <= 100 ==> O(1)


# Solution 2: Space-optimized Binary Search
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_rank = min(ranks)

        left = 1
        right = min_rank * (cars ** 2)

        while left <= right:
            middle = (left + right) // 2

            total_cars_repaired = 0
            for rank in ranks:
                total_cars_repaired += int(sqrt(middle / rank))

            if total_cars_repaired >= cars:
                right = middle - 1
            else:
                left = middle + 1
        
        return left

# n = len(ranks), m = number of cars, k = number of possible ranks
# Time Complexity: O(n * log(min_rank * m ^ 2) ==> O(n * log(min_rank * m)
# Space Complexity: O(1)
