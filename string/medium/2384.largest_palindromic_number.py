"""
Problem Number: 2384. Largest Palindromic Number
Difficulty Level: Medium
Link: https://leetcode.com/problems/largest-palindromic-number/

********************************************************************************

You are given a string num consisting of digits only.
Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.
Notes:
You do not need to use all the digits of num, but you must use at least one digit.
The digits can be reordered.

Example 1:
Input: num = "444947137"
Output: "7449447"
Explanation:
Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
It can be shown that "7449447" is the largest palindromic integer that can be formed.

Example 2:
Input: num = "00009"
Output: "9"
Explanation:
It can be shown that "9" is the largest palindromic integer that can be formed.
Note that the integer returned should not contain leading zeroes.

Constraints:
1 <= num.length <= 10^5
num consists of digits.
"""


class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = [0] * 10
        for digit in num:
            count[int(digit)] += 1

        first_half = []

        # 1. Process digits 9 down to 0
        for digit in range(9, -1, -1):
            if digit == 0 and not first_half:
                continue

            pairs = count[digit] // 2
            if pairs > 0:
                first_half.append(str(digit) * pairs)

        # 2. Determine Middle: The largest digit with an odd count
        middle = ""
        for digit in range(9, -1, -1):
            if count[digit] % 2 == 1:
                middle = str(digit)
                break

        if not first_half and not middle:
            return "0"

        return "".join(first_half) + middle + "".join(first_half[::-1])

# n = len(num)
# Time Complexity: O(3 * n) => O(n)
# Space Complexity: O(n)
