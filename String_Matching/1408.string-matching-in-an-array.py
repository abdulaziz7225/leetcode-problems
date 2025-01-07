"""
Problem Number: 1408. String Matching in an Array
Difficulty Level: Easy
https://leetcode.com/problems/string-matching-in-an-array

********************************************************************************

Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
A substring is a contiguous sequence of characters within a string
  
Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
  
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.
"""

from typing import List

# Solution 1
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
    
# Time Complexity: O(m^2 + n^2)
# Space Complexity: O(m + n)

# class Solution:
#     def stringMatching(self, words: List[str]) -> List[str]:
        
        
#         def construct_lps(pattern, lps):
#             ptr = 0
#             i = 1
            
#             while i < m:
#                 if pattern[i] == pattern[ptr]:
#                     ptr += 1
#                     lps[i] = ptr 
#                     i += 1
#                 elif ptr != 0:
#                     ptr = lps[ptr-1]
#                 else:
#                     lps[i] = 0
#                     i += 1
                    
#         for a in words:
#             pattern = words[a]
#             m = len(pattern)
#             lps = [0] * m
#             for b in range(len(words)):
#                 if a != b:
#                     n = len(words[b])
#                     construct_lps(pattern, lps)
            
        
#         print(lps)
#         result = 0
#         i = 0
#         j = 0
#         while i < n:
#             if word[i] == pat[j]:
#                 i += 1
#                 j += 1
#                 if j == m:
#                     result += 1
#             else:
#                 if j != 0:
#                     j = lps[j-1]
#                 else:
#                     i += 1
                
#         return result
    
obj = Solution()
print(obj.stringMatching("abcab"))