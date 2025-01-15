"""
Problem Number: 3304. Find the K-th Character in String Game I
Difficulty Level: Easy
https://leetcode.com/problems/find-the-k-th-character-in-string-game-i

********************************************************************************

Alice and Bob are playing a game. Initially, Alice has a string word = "a". You are given a positive integer k. Now Bob will 
ask Alice to perform the following operation forever: Generate a new string by changing each character in word to its next 
character in the English alphabet, and append it to the original word. For example, performing the operation on "c" generates 
"cd" and performing the operation on "zb" generates "zbac". Return the value of the kth character in word, after enough  
operations have been done for word to have at least k characters. Note that the character 'z' can be changed to 'a' in the 
operation.
  
Example 1:
Input: k = 5
Output: "b"
Explanation:
Initially, word = "a". We need to do the operation three times:
Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".

Example 2:
Input: k = 10
Output: "c"
  
Constraints:
1 <= k <= 500
"""

# Solution 1
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            temp = ""
            for char in word:
                next_char = ord(char) - ord('a') + 1
                temp += chr(next_char % 26 + ord('a'))
            word += temp
        return word[k-1]

# Time Complexity: O(k)
# Space Complexity: O(k)

# Solution 2
"""
The string will be constructed such that the indices of the same character share a specific commonality: the number of ones in the binary representation of the indices for the same character is always the same.

Index of 'a' = 0
Index of 'b' = 1, 2, 4, 8, ... (only one 1 in binary form)
Index of 'c' = 3, 5, 6, 9, 10, 12, ... (two 1s in binary form)
Index of 'd' = 7, 11, 13, 14, ... (three 1s in binary form)
Thus, we can derive the character at index ( k-1 ) by analyzing the number of ones in its binary representation.
"""

class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        return chr(ord('a') + bin(k - 1).count("1"))

# Time Complexity: O(1)
# Space Complexity: O(1)
