"""
Problem Number: 260. Single Number III
Difficulty Level: Medium
Link: https://leetcode.com/problems/single-number-iii/

********************************************************************************

Given an integer array nums, in which exactly two elements appear only once and all the
other elements appear exactly twice. Find the two elements that appear only once. You
can return the answer in any order. You must write an algorithm that runs in linear
runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]

Constraints:
2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_of_pairs = 0
        for num in nums:
            xor_of_pairs ^= num

        diff_bit = 1
        while not (xor_of_pairs & diff_bit):
            diff_bit = diff_bit << 1

        first = 0
        second = 0
        for num in nums:
            if num & diff_bit:
                first ^= num
            else:
                second ^= num
        
        return [first, second]

# Time Complexity: O(n)
# Space Complexity: O(1)
