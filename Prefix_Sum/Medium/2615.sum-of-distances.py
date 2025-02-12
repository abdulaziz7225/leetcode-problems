"""
Problem Number: 2615. Sum of Distances
Difficulty Level: Medium
https://leetcode.com/problems/sum-of-distances

********************************************************************************

You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of 
|i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0. Return the array arr.
  
Example 1:
Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

Example 2:
Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.
  
Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
Note: This question is the same as 2121: Intervals Between Identical Elements.
"""

from typing import List
from collections import defaultdict


# Solution 1
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prefix = {}
        result = []
        for i, num in enumerate(nums):
            prefix.setdefault(num, [])
            prefix[num].append(i)

        for i, num in enumerate(nums):
            curr = 0
            for j in prefix[num]:
                curr += abs(i - j)
            result.append(curr)

        return result

# Time Complexity: O(n^2)
# Space Complexity: O(n)


# Solution 2
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index_sums = {}  # Stores cumulative sum of indices for each unique number
        index_counts = {}  # Stores count of occurrences of each number up to current index
        result = []

        # First pass: Compute cumulative index sums and count occurrences
        for i, num in enumerate(nums):
            if num not in index_sums:
                index_counts[i] = 0
                index_sums[num] = [i]
            else:
                index_counts[i] = len(index_sums[num])
                index_sums[num].append(i + index_sums[num][-1])

                # Second pass: Compute the sum of distances using prefix and suffix contributions
        for i, num in enumerate(nums):
            # Count of occurrences before current index
            count_before = index_counts[i]
            cum_sum = index_sums[num]  # Cumulative sum array for the number
            prefix_sum = i * (count_before + 1) - cum_sum[count_before]
            suffix_sum = cum_sum[-1] - cum_sum[count_before] - \
                i * (len(cum_sum) - count_before - 1)
            result.append(prefix_sum + suffix_sum)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 3
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        # Stores sum of indices encountered so far
        prefix_count = defaultdict(int)
        prefix_sum = defaultdict(int)  # Stores count of occurrences

        # First pass: Compute prefix contributions
        for i, num in enumerate(nums):
            if prefix_count[num] > 0:
                result[i] += i * prefix_count[num] - prefix_sum[num]

            prefix_count[num] += 1
            prefix_sum[num] += i

        suffix_sum = defaultdict(int)
        suffix_count = defaultdict(int)

        # Second pass: Compute suffix contributions
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if suffix_count[num] > 0:
                result[i] += suffix_sum[num] - i * suffix_count[num]
            suffix_count[num] += 1
            suffix_sum[num] += i

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
