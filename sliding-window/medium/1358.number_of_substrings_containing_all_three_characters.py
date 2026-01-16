"""
Problem Number: 1358. Number of Substrings Containing All Three Characters
Difficulty Level: Medium
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

********************************************************************************

Given a string s consisting only of characters a, b and c. Return the number of
substrings containing at least one occurrence of all these characters a, b and c.
  
Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1
  
Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""


# Solution 1: Sliding Window
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq_map = {}
        left = right = 0
        result = 0
        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1

            while len(freq_map) == 3:
                result += len(s) - right
                freq_map[s[left]] -= 1
                if freq_map[s[left]] == 0:
                    del freq_map[s[left]]
                left += 1
        return result

# n = length of string, k = number of characters
# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(k) ==> O(1)


# Solution 2: Last Position Tracking
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_position = [-1] * 3
        result = 0
        for idx, char in enumerate(s):
            last_position[ord(char) - ord('a')] = idx
            result += min(last_position) + 1
        return result

# n = length of string, k = number of characters
# Time Complexity: O(n)
# Space Complexity: O(k) ==> O(1)
