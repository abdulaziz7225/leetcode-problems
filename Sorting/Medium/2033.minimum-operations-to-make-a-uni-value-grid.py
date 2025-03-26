"""
Problem Number: 2033. Minimum Operations to Make a Uni-Value Grid
Difficulty Level: Medium
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

********************************************************************************

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
A uni-value grid is a grid where all the elements of it are equal.
Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
  
Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

Example 2:
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.

Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
  
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
1 <= x, grid[i][j] <= 10^4
"""

from typing import List

"""
Assume the sorted array is [a, b, c, d], x = 1
If we choose b as median, then the answer will be:
(b - a) + (c - b) + (d - b) = (c + d) - (a + b)

If we choose c as median, then the answer will be:
(c - a) + (c - b) + (d - c) = (c + d) - (a + b)

This prove that both median can get the same answer.
"""


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        array_1D = []
        common_remainder = grid[0][0] % x

        for row in grid:
            for num in row:
                if num % x != common_remainder:
                    return -1
                array_1D.append(num)

        array_1D.sort()
        median = array_1D[len(array_1D) // 2]
        result = 0
        for num in array_1D:
            result += abs(num - median) // x

        return result

# m = number of rows, n = number of columns
# Time Complexity: O(m * n * log(m * n)) + 2 * O(m * n) ==> O(m * n * log(m * n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(m * n) additional space.
# Space Complexity: O(2 * m * n) ==> O(m * n)
