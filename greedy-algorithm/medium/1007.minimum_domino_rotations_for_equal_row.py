"""
Problem Number: 1007. Minimum Domino Rotations For Equal Row
Difficulty Level: Medium
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row

********************************************************************************

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
If it cannot be done, return -1.
  
Example 1:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
  
Constraints:
2 <= tops.length <= 2 * 10^4
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
"""

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result1 = self.check(tops, bottoms, tops[0])
        result2 = self.check(tops, bottoms, bottoms[0])

        if result1 * result2 < 0:
            return max(result1, result2)
        return min(result1, result2)

    def check(self, tops: List[int], bottoms: List[int], candidate) -> int:
        top_rotation, bottom_rotation = 0, 0

        for i in range(len(tops)):
            if tops[i] != candidate and bottoms[i] != candidate:
                return -1

            if candidate != tops[i]:
                top_rotation += 1
            if candidate != bottoms[i]:
                bottom_rotation += 1

        return min(top_rotation, bottom_rotation)

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(1)
