"""
Problem Number: 457. Circular Array Loop
Difficulty Level: Medium
Link: https://leetcode.com/problems/circular-array-loop

********************************************************************************

You are playing a game involving a circular array of non-zero integers nums. Each
nums[i] denotes the number of indices forward/backward you must move if you are located
at index i:
If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move abs(nums[i]) steps backward.
Since the array is circular, you may assume that moving forward from the last element
puts you on the first element, and moving backwards from the first element puts you on
the last element.
A cycle in the array consists of a sequence of indices seq of length k where:
Following the movement rules above results in the repeating index sequence seq[0] ->
seq[1] -> ... -> seq[k - 1] -> seq[0] -> ... Every nums[seq[j]] is either all positive
or all negative. k > 1
Return true if there is a cycle in nums, or false otherwise.

Example 1:
Input: nums = [2,-1,1,2,2]
Output: true
Explanation: The graph shows how the indices are connected. White nodes are jumping
forward, while red is jumping backward. We can see the cycle 0 --> 2 --> 3 --> 0 -->
..., and all of its nodes are white (jumping in the same direction).

Example 2:
Input: nums = [-1,-2,-3,-4,-5,6]
Output: false
Explanation: The graph shows how the indices are connected. White nodes are jumping
forward, while red is jumping backward. The only cycle is of size 1, so we return false.

Example 3:
Input: nums = [1,-1,5,1,4]
Output: true
Explanation: The graph shows how the indices are connected. White nodes are jumping
forward, while red is jumping backward. We can see the cycle 0 --> 1 --> 0 --> ..., and
while it is of size > 1, it has a node jumping forward and a node jumping backward, so
it is not a cycle. We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are
white (jumping in the same direction).

Constraints:
1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0

Follow up: Could you solve it in O(n) time complexity and O(1) extra space complexity?
"""

from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def get_next(index: int) -> int:
            return (index + nums[index]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i
            direction = 1 if nums[i] > 0 else -1

            while (nums[fast] * direction > 0 and nums[get_next(fast)] * direction > 0):
                slow = get_next(slow)
                fast = get_next(get_next(fast))

                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True

            slow = i
            while nums[slow] * direction > 0:
                next_index = get_next(slow)
                nums[slow] = 0
                slow = next_index

        return False


# Every element is visited a constant number of times. Once an element is part of a failed path, it is set to 0 and never checked again.
# Time Complexity: O(n)
# Space Complexity: O(1)
