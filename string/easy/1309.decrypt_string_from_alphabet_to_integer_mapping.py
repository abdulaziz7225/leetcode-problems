"""
Problem Number: 1309. Decrypt String from Alphabet to Integer Mapping
Difficulty Level: Easy
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping

********************************************************************************

You are given a string s formed by digits and '#'. We want to map s to English lowercase
characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.
The test cases are generated so that a unique mapping will always exist.
  
Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"
  
Constraints:
1 <= s.length <= 1000
s consists of digits and the '#' letter.
s will be a valid string such that mapping is always possible.
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        l1 = len(s)
        result = []

        while i < l1:
            if i + 2 < l1 and s[i + 2] == "#":
                temp = chr(int(s[i:i+2]) + 96)
                i += 3
            else:
                temp = chr(int(s[i]) + 96)
                i += 1
            result.append(temp)

        return "".join(result)

# Time Complexity: O(n)
# Space Complexity: O(n)
