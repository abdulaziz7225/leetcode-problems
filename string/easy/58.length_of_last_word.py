"""
Problem Number: 58. Length of Last Word
Difficulty Level: Easy
https://leetcode.com/problems/length-of-last-word

********************************************************************************

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal
substring
consisting of non-space characters only.
  
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
  
Constraints:
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_occurred = False
        start_index = -1
        last_index = len(s) - 1
        
        for i in range(len(s) - 1, -1, -1):
            if not last_word_occurred and s[i].isalpha():
                last_word_occurred = True
                last_index = i
            if last_word_occurred and s[i] == " ":
                start_index = i
                break

        return last_index - start_index
    
# Time Complexity: O(n)
# Space Complexity: O(1)
