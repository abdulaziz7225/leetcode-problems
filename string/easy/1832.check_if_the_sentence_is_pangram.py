"""
Problem Number: 1832. Check if the Sentence Is Pangram
Difficulty Level: Easy
Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/

********************************************************************************

A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false

Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""


# Solution 1: Hash Set
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        for char in sentence:
            letters.add(char)
        return len(letters) == 26

# Time Complexity: O(n)
# Space Complexity: O(26) ==> O(1)


# Solution 2: Bit Manipulation
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = (1 << 26) - 1
        temp = 0

        for char in sentence:
            temp |= 1 << (ord(char) - ord("a"))
            if temp == pangram:
                return True
        
        return False

# Time Complexity: O(n)
# Space Complexity: O(1)
