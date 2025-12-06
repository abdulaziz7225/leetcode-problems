"""
Problem Number: 2270. Number of Ways to Split Array
Difficulty Level: Medium
https://leetcode.com/problems/number-of-ways-to-split-array/

********************************************************************************

You are given a 0-indexed integer array nums of length n. nums contains a valid split at index i if the following are 
true: The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements. There is at 
least one element to the right of i. That is, 0 <= i < n - 1. Return the number of valid splits in nums.

Example 1:
Input: nums = [10,4,-8,7]
Output: 2
Explanation: 
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. 
Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. 
Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. 
Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.

Example 2:
Input: nums = [2,3,1,0]
Output: 2
Explanation: 
There are two valid splits in nums:
- Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. 
Since 5 >= 1, i = 1 is a valid split. 
- Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. 
Since 6 >= 0, i = 2 is a valid split.
 
Constraints:
2 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
"""

from typing import List

# Solution 1
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        initial_value = 0
        prefix = []

        for num in nums:
            initial_value += num
            prefix.append(initial_value)

        result = 0
        for i in range(len(prefix)-1):
            if 2 * prefix[i] >= prefix[-1]:
                result += 1
        return result
        
# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 2
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        result = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                result += 1
        return result
        
# Time Complexity: O(n)
# Space Complexity: O(1)