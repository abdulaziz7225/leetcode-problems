"""
Problem Number: 241. Different Ways to Add Parentheses
Difficulty Level: Medium
Link: https://leetcode.com/problems/different-ways-to-add-parentheses

********************************************************************************

Given a string expression of numbers and operators, return all possible results from
computing all the different possible ways to group numbers and operators. You may return
the answer in any order. The test cases are generated such that the output values fit in
a 32-bit integer and the number of different results does not exceed 104.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
"""

from typing import List


# Solution 1: Recursion
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []

        if len(expression) == 0:
            return results
        elif len(expression) == 1 or (len(expression) == 2 and expression[0].isdigit()):
            return [int(expression)]

        for index, curr_char in enumerate(expression):
            if curr_char.isdigit():
                continue

            left_results = self.diffWaysToCompute(expression[:index])
            right_results = self.diffWaysToCompute(expression[index + 1:])

            for left_value in left_results:
                for right_value in right_results:
                    if curr_char == "+":
                        results.append(left_value + right_value)
                    elif curr_char == "-":
                        results.append(left_value - right_value)
                    elif curr_char == "*":
                        results.append(left_value * right_value)

        return results

# Time Complexity: O(n * 2^n)
# Space Complexity: O(2^n)


# Solution 2: Memoization
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.memo = dict()
        return self._compute_results(expression, 0, len(expression) - 1)

    def _compute_results(self, expression: str, start: int, end: int) -> List[int]:
        if (start, end) in self.memo:
            return self.memo[(start, end)]

        results = []

        if start == end or (end - start == 1 and expression[start].isdigit()):
            results.append(int(expression[start:end + 1]))
            return results

        for index in range(start, end + 1):
            curr_char = expression[index]

            if curr_char.isdigit():
                continue

            left_results = self._compute_results(expression, start, index - 1)
            right_results = self._compute_results(expression, index + 1, end)

            for left_value in left_results:
                for right_value in right_results:
                    if curr_char == "+":
                        results.append(left_value + right_value)
                    elif curr_char == "-":
                        results.append(left_value - right_value)
                    elif curr_char == "*":
                        results.append(left_value * right_value)

        self.memo[(start, end)] = results
        return results

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n^2 * 2^n)
