"""
Problem Number: 2843. Count Symmetric Integers
Difficulty Level: Easy
https://leetcode.com/problems/count-symmetric-integers

********************************************************************************

You are given two positive integers low and high.
An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of
x is equal to the sum of the last n digits of x. Numbers with an odd number of digits
are never symmetric. Return the number of symmetric integers in the range [low, high].
  
Example 1:
Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:
Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
  
Constraints:
1 <= low <= high <= 10^4
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            if self.is_symmetric(num):
                count += 1
        return count

    def is_symmetric(self, num):
        num_to_arr = []

        while num > 0:
            num, r = divmod(num, 10)
            num_to_arr.append(r)

        n = len(num_to_arr)
        if n & 1 == 1:
            return False

        result = 0
        for i in range(n // 2):
            result += num_to_arr[i] - num_to_arr[n - i - 1]

        return result == 0

# n = number of integers, m = number of digits in each number
# Time Complexity: O(n * m)
# Space Complexity: O(1)
