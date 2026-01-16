"""
Problem Number: 2563. Count the Number of Fair Pairs
Difficulty Level: Medium
https://leetcode.com/problems/count-the-number-of-fair-pairs

********************************************************************************

Given a 0-indexed integer array nums of size n and two integers lower and upper, return
the number of fair pairs. A pair (i, j) is fair if:
0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
  
Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
  
Constraints:
1 <= nums.length <= 10^5
nums.length == n
-10^9 <= nums[i] <= 10^9
-10^9 <= lower <= upper <= 10^9
"""

from typing import List


# Solution 1: Two Pointers Approach
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, array, target) -> int:
        left, right = 0, len(array) - 1
        count = 0
        while left < right:
            if array[left] + array[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

# Time Complexity: O(n * log(n))
# Space Complexity: O(n)
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.


# Solution 2: Binary Search Approach
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0

        for i, num in enumerate(nums):
            lower_index = self.lower_bound(nums, lower - num, i + 1)
            upper_index = self.lower_bound(nums, upper - num + 1, i + 1)
            count += upper_index - lower_index

        return count

    def lower_bound(self, array, target, left) -> int:
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2
            if array[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return left

# Time Complexity: O(n * log(n))
# Space Complexity: O(n)
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
