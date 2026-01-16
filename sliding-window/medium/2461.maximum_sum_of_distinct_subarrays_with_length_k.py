"""
Problem Number: 2461. Maximum Sum of Distinct Subarrays With Length K
Difficulty Level: Medium
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

********************************************************************************

You are given an integer array nums and an integer k. Find the maximum subarray sum of
all the subarrays of nums that meet the following conditions: The length of the subarray
is k, and All the elements of the subarray are distinct. Return the maximum subarray sum
of all the subarrays that meet the conditions. If no subarray meets the conditions,
return 0. A subarray is a contiguous non-empty sequence of elements within an array.
  
Example 1:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
  
Constraints:
1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from typing import List


# Solution 1
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        unique_nums = set()
        curr_sum = 0
        max_subarray_sum = 0

        for right, num in enumerate(nums):
            if num in unique_nums:
                left = right - len(unique_nums)
                while nums[left] != num:
                    curr_sum -= nums[left]
                    unique_nums.remove(nums[left])
                    left += 1
            else:
                unique_nums.add(num)
                curr_sum += num
                if len(unique_nums) > k:
                    curr_sum -= nums[right - k]
                    unique_nums.remove(nums[right - k])
                if len(unique_nums) == k:
                    max_subarray_sum = max(max_subarray_sum, curr_sum)

        return max_subarray_sum


# Handling duplicate elements (while nums[j] != num). In the worst case, this loop runs up to O(k) times for each duplicate.
# However, since j moves forward while idx moves forward, each element is removed from unique_nums at most once.
# So overall, the worst-case cost across the entire loop is O(N).
# Time Complexity: O(n)
# Space Complexity: O(k)


# Solution 2
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_to_index = {}
        curr_sum = 0
        max_subarray_sum = 0
        left = 0

        for right, curr_num in enumerate(nums):
            last_occurrence = num_to_index.get(curr_num, -1)
            while left <= last_occurrence or right - left + 1 > k:
                curr_sum -= nums[left]
                left += 1

            num_to_index[curr_num] = right
            curr_sum += curr_num
            if right - left + 1 == k:
                max_subarray_sum = max(max_subarray_sum, curr_sum)

        return max_subarray_sum

# Time Complexity: O(n)
# Space Complexity: O(n)
