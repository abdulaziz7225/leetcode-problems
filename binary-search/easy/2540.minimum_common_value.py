"""
Problem Number: 2540. Minimum Common Value
Difficulty Level: Easy
https://leetcode.com/problems/minimum-common-value

********************************************************************************

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the
minimum integer common to both arrays. If there is no common integer amongst nums1 and
nums2, return -1. Note that an integer is said to be common to nums1 and nums2 if both
arrays have at least one occurrence of that integer.
  
Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the
smallest, so 2 is returned.
  
Constraints:
1 <= nums1.length, nums2.length <= 10^5
1 <= nums1[i], nums2[j] <= 10^9
Both nums1 and nums2 are sorted in non-decreasing order.
"""

from typing import List


# Solution 1: Two Pointers
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return -1

# n = len(nums1), m = len(nums2)
# Time Complexity: O(n + m)
# Space Complexity: O(1)


# Solution 2: Binary Search
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)

        for num in nums1:
            if self.binary_search(nums2, num):
                return num

        return -1

    def binary_search(self, array: List[int], target: int) -> bool:
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if array[middle] == target:
                return True
            elif array[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False

# n = len(nums1), m = len(nums2)
# Time Complexity: O(n * log(n))
# Space Complexity: O(1)
