"""
Problem Number: 1636. Sort Array by Increasing Frequency
Difficulty Level: Easy
Link: https://leetcode.com/problems/sort-array-by-increasing-frequency

********************************************************************************

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.

Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""

from typing import List


# Solution 1: Lambda function
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        return sorted(nums, key=lambda x: (freq[x], -x))

# Time Complexity: O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * n) => O(n)


# Solution 2: Custom Merge Sort
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        self.custom_merge_sort(nums, 0, len(nums) - 1, freq)
        return nums

    def custom_merge_sort(self, array, left, right, freq):
        if left < right:
            middle = (left + right) // 2

            self.custom_merge_sort(array, left, middle, freq)
            self.custom_merge_sort(array, middle + 1, right, freq)

            self.custom_merge(array, left, middle, right, freq)

    def custom_merge(self, array, left, middle, right, freq):
        n1 = middle - left + 1
        n2 = right - middle

        left_array = array[left:middle + 1]
        right_array = array[middle + 1:right + 1]

        i = j = 0
        k = left
        while i < n1 and j < n2:
            if (freq[left_array[i]] < freq[right_array[j]]) or \
                    (freq[left_array[i]] == freq[right_array[j]] and left_array[i] > right_array[j]):
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < n1:
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < n2:
            array[k] = right_array[j]
            j += 1
            k += 1

# Time Complexity: O(n * log(n) + n) ==> O(n * log(n))
# Space Complexity: O(2 * n + log(n)) ==> O(n)
