"""
Problem Number: 646. Maximum Length of Pair Chain
Difficulty Level: Medium
Link: https://leetcode.com/problems/maximum-length-of-pair-chain

********************************************************************************

You are given an array of n pairs pairs where pairs[i] = [left[i], right[i]] and left[i]
< right[i]. A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can
be formed in this fashion.
Return the length longest chain which can be formed.
You do not need to use up all the given intervals. You can select pairs in any order.

Example 1:
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].

Example 2:
Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

Constraints:
n == pairs.length
1 <= n <= 1000
-1000 <= left[i] < right[i] <= 1000
"""

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        length = 0
        end_point = float('-inf')

        for pair in pairs:
            if pair[0] > end_point:
                end_point = pair[1]
                length += 1

        return length

# Time Complexity: O(n * log(n) + n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)
