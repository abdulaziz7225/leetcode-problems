"""
Problem Number: 1502. Can Make Arithmetic Progression From Sequence
Difficulty Level: Easy
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

********************************************************************************

A sequence of numbers is called an arithmetic progression if the difference between any
two consecutive elements is the same. Given an array of numbers arr, return true if the
array can be rearranged to form an arithmetic progression. Otherwise, return false.
  
Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2
respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
  
Constraints:
2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""

from typing import List


# Solution 1
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)-2):
            if arr[i] + arr[i+2] != 2 * arr[i+1]:
                return False
        return True

# Time Complexity: O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)


# Solution 2
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        max_val = max(arr)
        min_val = min(arr)
        step = (max_val - min_val) / (len(arr) - 1)

        if step == 0:
            return True

        i = 0
        while i < len(arr):
            if arr[i] == min_val + i * step:
                i += 1
            else:
                diff = arr[i] - min_val
                if diff % step != 0:
                    return False
                pos = int(diff / step)
                if arr[pos] == arr[i]:
                    return False
                arr[pos], arr[i] = arr[i], arr[pos]
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)
