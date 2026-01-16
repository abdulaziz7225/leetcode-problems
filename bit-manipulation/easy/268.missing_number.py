"""
Problem Number: 268. Missing Number
Difficulty Level: Easy
https://leetcode.com/problems/missing-number

********************************************************************************

Given an array nums containing n distinct numbers in the range [0, n], return the only
number in the range that is missing from the array.
  
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing
number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing
number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing
number in the range since it does not appear in nums.
          
Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.
  Follow up: Could you implement a solution using only O(1) extra space complexity and
  O(n) runtime complexity?
"""

from typing import List


# Solution 1: Arithmetic Sum
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n * (n + 1) // 2
        for num in nums:
            result -= num
        return result

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 2: XOR Operation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for idx, num in enumerate(nums):
            result ^= (idx + 1) ^ num
        return result

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 3: Index Operation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for idx, num in enumerate(nums):
            result += idx - num
        return result

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 4: Cyclic Sort
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i]
            if j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i

        return n

# Time Complexity: O(3 * n - 1) ==> O(n)
# Space Complexity: O(1)