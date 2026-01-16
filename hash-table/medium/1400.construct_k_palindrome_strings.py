"""
Problem Number: 1400. Construct K Palindrome Strings
Difficulty Level: Medium
https://leetcode.com/problems/construct-k-palindrome-strings

********************************************************************************

Given a string s and an integer k, return true if you can use all the characters in s to
construct k palindrome strings or false otherwise.
  
Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
  
Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= 10^5
"""


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        elif len(s) < k:
            return False

        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        odd_freq = 0
        for freq in freq:
            if freq % 2 == 1:
                odd_freq += 1
        return odd_freq <= k
    
# n = len(s)
# Time Complexity: O(n)
# Space Complexity: O(1)
