"""
Problem Number: 4. Median of Two Sorted Arrays
Difficulty Level: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

********************************************************************************

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
median of the two sorted arrays. The overall run time complexity should be O(log
(m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


# Solution 1: Merge Two Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = []
        n = len(nums1)
        m = len(nums2)
        i, j = 0, 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merged_list.append(nums1[i])
                i += 1
            else:
                merged_list.append(nums2[j])
                j += 1

        while i < n:
            merged_list.append(nums1[i])
            i += 1
        while j < m:
            merged_list.append(nums2[j])
            j += 1

        size = len(merged_list)
        if size % 2 == 1:
            return merged_list[size // 2]
        return (merged_list[size // 2 - 1] + merged_list[size // 2]) / 2

# n = len(nums1), m = len(nums2)
# Time Complexity: O(n + m)
# Time Complexity: O(n + m)


# Solution 2: Two Pointers
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        size = n + m

        ptr1, ptr2 = 0, 0
        prev, curr = 0, 0

        for _ in range(size // 2 + 1):
            prev = curr

            if ptr1 < n and (ptr2 == m or nums1[ptr1] < nums2[ptr2]):
                curr = nums1[ptr1]
                ptr1 += 1
            else:
                curr = nums2[ptr2]
                ptr2 += 1

        if size % 2 == 0:
            return (prev + curr) / 2
        return curr

# n = len(nums1), m = len(nums2)
# Time Complexity: O(n + m)
# Time Complexity: O(1)


# Solution 3: Binary Search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        n = len(nums1)
        m = len(nums2)
        size = (n + m)
        half_size = (size + 1) // 2

        left = 0
        right = n

        while left <= right:
            partA = (left + right) // 2
            partB = half_size - partA

            maxLeftA = float("-inf") if partA == 0 else nums1[partA - 1]
            minRightA = float("inf") if partA == n else nums1[partA]
            maxLeftB = float("-inf") if partB == 0 else nums2[partB - 1]
            minRightB = float("inf") if partB == m else nums2[partB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if size % 2 == 1:
                    return max(maxLeftA, maxLeftB)
                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            elif maxLeftA < minRightB:
                left = partA + 1
            else:
                right = partA - 1

        return -0.0

# n = len(nums1), m = len(nums2)
# Time Complexity: O(log(min(n, m)))
# Time Complexity: O(1)
