"""
Problem Number: 1232. Check If It Is a Straight Line
Difficulty Level: Easy
https://leetcode.com/problems/check-if-it-is-a-straight-line

********************************************************************************

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the
coordinate of a point. Check if these points make a straight line in the XY plane.
    
Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
  
Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l1 = len(coordinates)
        (x0, y0), (x1, y1) = coordinates[:2]
        for i in range(2, l1):
            x, y = coordinates[i]
            if (y1 - y0) * (x - x1) != (y - y1) * (x1 - x0):
                return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)
