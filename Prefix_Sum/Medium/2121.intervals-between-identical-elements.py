"""
Problem Number: 2121. Intervals Between Identical Elements
Difficulty Level: Medium
https://leetcode.com/problems/intervals-between-identical-elements

********************************************************************************

You are given a 0-indexed array of n integers arr.
The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the 
interval between arr[i] and arr[j] is |i - j|. Return an array intervals of length n where intervals[i] is the sum of intervals 
between arr[i] and each element in arr with the same value as arr[i].
Note: |x| is the absolute value of x.
  
Example 1:
Input: arr = [2,1,3,1,2,3,3]
Output: [4,2,7,2,4,4,5]
Explanation:
- Index 0: Another 2 is found at index 4. |0 - 4| = 4
- Index 1: Another 1 is found at index 3. |1 - 3| = 2
- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
- Index 3: Another 1 is found at index 1. |3 - 1| = 2
- Index 4: Another 2 is found at index 0. |4 - 0| = 4
- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5

Example 2:
Input: arr = [10,5,10,10]
Output: [5,0,3,4]
Explanation:
- Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
- Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
- Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
- Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4
  
Constraints:
n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= 10^5
Note: This question is the same as 2615: Sum of Distances.
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
