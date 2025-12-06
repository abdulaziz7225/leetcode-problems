"""
Problem Number: 1961. Check If String Is a Prefix of Array
Difficulty Level: Easy
https://leetcode.com/problems/check-if-string-is-a-prefix-of-array

********************************************************************************

Given a string s and an array of strings words, determine whether s is a prefix string of words.
A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.
Return true if s is a prefix string of words, or false otherwise.
  
Example 1:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:
Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
  
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] and s consist of only lowercase English letters.
"""

from typing import List


# Solution 1
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        number_of_words, i = 0, 0
        n = len(s)

        while n > 0 and number_of_words < len(words):
            number_of_words += 1
            n -= len(words[i])
            i += 1

        return s == "".join(words[:number_of_words])

# n = len(s), k = len(words)
# m = length of longest word in the given array
# Time Complexity: O(n + m) ==> O(n)
# Space Complexity: O(n)


# Solution 2
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        curr_index = 0

        for word in words:
            if s[curr_index:curr_index + len(word)] != word:
                return False
            curr_index += len(word)

            if curr_index == len(s):
                return True
            elif curr_index > len(s):
                break
        return False

# n = len(s), k = len(words)
# m = length of longest word in the given array
# Time Complexity: O(n)
# Space Complexity: O(m)
