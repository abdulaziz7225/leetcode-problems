"""
Problem Number: 1512. Number of Good Pairs
Difficulty Level: Easy
Link: https://leetcode.com/problems/number-of-good-pairs

********************************************************************************

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from typing import List


# Solution 1
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = 0
        for freq in count.values():
            result += freq * (freq - 1) // 2
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 2
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = dict()
        result = 0

        for num in nums:
            if num in count:
                result += count[num]
            count[num] = count.get(num, 0) + 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
