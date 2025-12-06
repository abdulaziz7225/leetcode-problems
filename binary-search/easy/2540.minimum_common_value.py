"""
Problem Number: 2540. Minimum Common Value
Difficulty Level: Easy
https://leetcode.com/problems/minimum-common-value

********************************************************************************

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
  
Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
  
Constraints:
1 <= nums1.length, nums2.length <= 10^5
1 <= nums1[i], nums2[j] <= 10^9
Both nums1 and nums2 are sorted in non-decreasing order.
"""

from typing import List


# Solution 1: Two Pointers
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return -1

# N = len(nums1), M = len(nums2)
# Time Complexity: O(N + M)
# Space Complexity: O(1)


# Solution 2: Binary Search
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            first, second = nums2, nums1
        else:
            first, second = nums1, nums2

        for target in first:
            if self.binary_search(second, target):
                return target
        return -1

    def binary_search(self, array: List[int], target: int) -> bool:
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2
            if array[middle] == target:
                return True
            elif array[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False

# N = len(first), M = len(second)
# Time Complexity: O(N * log(M))
# Space Complexity: O(1)
