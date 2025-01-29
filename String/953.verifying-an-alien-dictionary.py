"""
Problem Number: 953. Verifying an Alien Dictionary
Difficulty Level: Easy
https://leetcode.com/problems/verifying-an-alien-dictionary

********************************************************************************

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
  
Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
  
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {letter: idx for idx, letter in enumerate(order)}

        for i in range(1, len(words)):
            first_word = words[i-1]
            second_word = words[i]
            min_len = min(len(first_word), len(second_word))
            for j in range(min_len):
                if alphabet[first_word[j]] > alphabet[second_word[j]]:
                    return False
                elif alphabet[first_word[j]] < alphabet[second_word[j]]:
                    break
            else:
                if len(first_word) > len(second_word):
                    return False
        return True

# M = len(words), N = average length of word in 'words' list
# Time Complexity: O(M * N)
# Space Complexity: O(1)
