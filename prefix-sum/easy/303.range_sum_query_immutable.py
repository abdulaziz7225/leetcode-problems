"""
Problem Number: 303. Range Sum Query - Immutable
Difficulty Level: Easy
https://leetcode.com/problems/range-sum-query-immutable

********************************************************************************

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
  
Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
  
Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= left <= right < nums.length
At most 10^4 calls will be made to sumRange.
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        curr = 0
        for num in nums:
            curr += num
            self.prefix_sum.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        result = self.prefix_sum[right]
        if left > 0:
            result -= self.prefix_sum[left - 1]
        return result

# Time Complexity:
# __init__() method: O(n)
# sumRange() method: O(1)
# Space Complexity: O(n)
