"""
Problem Number: 2131. Longest Palindrome by Concatenating Two Letter Words
Difficulty Level: Medium
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

********************************************************************************

You are given an array of strings words. Each element of words consists of two lowercase
English letters. Create the longest possible palindrome by selecting some elements from
words and concatenating them in any order. Each element can be selected at most once.
Return the length of the longest palindrome that you can create. If it is impossible to
create any palindrome, return 0. A palindrome is a string that reads the same forward
and backward.
  
Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
  
Constraints:
1 <= words.length <= 10^5
words[i].length == 2
words[i] consists of lowercase English letters.
"""

from typing import List


# Solution 1
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result = 0
        middle = 0
        hash_map = {}
        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1

        for word, freq in hash_map.items():
            pair = word[::-1]
            if word == pair:
                result += 2 * (freq // 2)
                if freq & 1 == 1:
                    middle = 1
            elif pair in hash_map:
                result += min(freq, hash_map[pair])

        return 2 * (result + middle)

# Time Complexity: O(n + 26 ^ 2) ==> O(n)
# Space Complexity: O(26 ^ 2) ==> O(1)


# Solution 2: Avoid double counting (only one direction)
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result = 0
        middle = 0
        hash_map = {}
        for word in words:
            hash_map[word] = hash_map.get(word, 0) + 1

        for word, freq in hash_map.items():
            pair = word[::-1]
            if word == pair:
                result += 2 * (freq // 2)
                if freq & 1 == 1:
                    middle = 1
            elif word < pair:  # Avoid double counting (only one direction)
                result += 2 * min(freq, hash_map.get(pair, 0))

        return 2 * (result + middle)

# Time Complexity: O(n + 26 ^ 2) ==> O(n)
# Space Complexity: O(26 ^ 2) ==> O(1)
