"""
Problem Number: 3121. Count the Number of Special Characters II
Difficulty Level: Medium
https://leetcode.com/problems/count-the-number-of-special-characters-ii

********************************************************************************

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
Return the number of special letters in word.
  
Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters are 'a', 'b', and 'c'.

Example 2:
Input: word = "abc"
Output: 0
Explanation:
There are no special characters in word.

Example 3:
Input: word = "AbBCab"
Output: 0
Explanation:
There are no special characters in word.
  
Constraints:
1 <= word.length <= 2 * 10^5
word consists of only lowercase and uppercase English letters.
"""


# Solution 1
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = [-1] * 26
        uppercase = [-1] * 26
        special_letters = 0

        for idx, char in enumerate(word):
            if char.islower():
                lowercase[ord(char) - ord("a")] = idx
            elif uppercase[ord(char) - ord("A")] == -1:
                uppercase[ord(char) - ord("A")] = idx

        for i in range(26):
            if lowercase[i] > -1 and lowercase[i] < uppercase[i]:
                special_letters += 1

        return special_letters

# Time Complexity: O(n + 52) ==> O(n)
# Space Complexity: O(52) ==> O(1)


# Solution 2
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowercase = [False] * 26
        uppercase = [False] * 26
        special_letters = 0

        for chr in word:
            if chr.islower():
                # If at least one uppercase letter appeared before, the lowercase becomes 'False'
                lowercase[ord(chr) - ord("a")] = not uppercase[ord(chr) - ord("a")]
            else:
                uppercase[ord(chr) - ord("A")] = True

        for i in range(26):
            special_letters += lowercase[i] and uppercase[i]

        return special_letters

# Time Complexity: O(n + 52) ==> O(n)
# Space Complexity: O(52) ==> O(1)
