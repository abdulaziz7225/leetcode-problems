"""
Problem Number: 345. Reverse Vowels of a String
Difficulty Level: Easy
Link: https://leetcode.com/problems/reverse-vowels-of-a-string

********************************************************************************

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
"""


# Solution 1: Stack
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for char in s:
            if char in vowels:
                stack.append(char)

        result = []
        for char in s:
            if char in vowels:
                result.append(stack.pop())
            else:
                result.append(char)

        return "".join(result)

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(n)


# Solution 2: Two Pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        array = list(s)
        left = 0
        right = len(array) - 1

        while left < right:
            while left < right and array[left] not in vowels:
                left += 1

            while left < right and array[right] not in vowels:
                right -= 1

            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

        return "".join(array)

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(n)
