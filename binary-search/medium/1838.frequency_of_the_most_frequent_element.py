"""
Problem Number: 1838. Frequency of the Most Frequent Element
Difficulty Level: Medium
Link: https://leetcode.com/problems/frequency-of-the-most-frequent-element

********************************************************************************

The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.

Example 1:
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:
Input: nums = [3,9,6], k = 2
Output: 1

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^5
"""

from typing import List


# Solution 1: Sliding Window
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        curr = 0
        left = 0

        for right in range(len(nums)):
            target = nums[right]
            curr += target

            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1

            result = max(result, right - left + 1)

        return result

# Time Complexity: O(n * log(n) + 2 * n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)


# Solution 2: Advanced Sliding Window
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = 0
        left = 0

        for right in range(len(nums)):
            target = nums[right]
            curr += target

            if (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1

        return len(nums) - left

# Time Complexity: O(n * log(n) + 2 * n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)


# Solution 3: Binary Search
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        prefix = []
        cum_sum = 0
        for num in nums:
            cum_sum += num
            prefix.append(cum_sum)

        result = 0
        for idx in range(len(nums)):
            result = max(result, self.check(nums, prefix, idx, k))

        return result

    def check(self, array: List[int], prefix: List[int], idx: int, k: int) -> int:
        left = 0
        right = idx
        target = array[idx]
        best = idx

        while left <= right:
            middle = (left + right) // 2
            count = idx - middle + 1

            final_sum = count * target
            original_sum = prefix[idx] - prefix[middle] + array[middle]
            operations_required = final_sum - original_sum

            if operations_required > k:
                left = middle + 1
            else:
                best = middle
                right = middle - 1

        return idx - best + 1

# Time Complexity: O(2 * n * log(n) + n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * n) ==> O(n)
