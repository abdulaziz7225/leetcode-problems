"""
Problem Number: 1346. Check If N and Its Double Exist
Difficulty Level: Easy
https://leetcode.com/problems/check-if-n-and-its-double-exist

********************************************************************************

Given an array arr of integers, check if there exist two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
  
Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
  
Constraints:
2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen_nums = set()
        for num in arr:
            if 2 * num in seen_nums or \
                    (num & 1 == 0 and num // 2 in seen_nums):
                return True
            seen_nums.add(num)
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
