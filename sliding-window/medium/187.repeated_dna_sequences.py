"""
Problem Number: 187. Repeated DNA Sequences
Difficulty Level: Medium
https://leetcode.com/problems/repeated-dna-sequences

********************************************************************************

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G',
and 'T'. For example, "ACGAATTCCG" is a DNA sequence. When studying DNA, it is useful to
identify repeated sequences within the DNA. Given a string s that represents a DNA
sequence, return all the 10-letter-long sequences (substrings) that occur more than once
in a DNA molecule. You may return the answer in any order.
  
Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
  
Constraints:
1 <= s.length <= 10^5
s[i] is either 'A', 'C', 'G', or 'T'.
"""

from typing import List


# Solution 1
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10
        seen_patterns = {}
        for i in range(len(s) - L + 1):
            curr_pattern = s[i:i + L]
            seen_patterns[curr_pattern] = seen_patterns.get(
                curr_pattern, 0) + 1

        result = []
        for pattern, freq in seen_patterns.items():
            if freq > 1:
                result.append(pattern)

        return result

# n = length of string, l = length of pattern
# Time Complexity: O((n - l) * l) ==> O(n * l)
# Space Complexity: O((n - l) * l) ==> O(n * l)


# Solution 2: Rolling Hash Technique and the Rabin-Karp Algorithm
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10  # length of pattern
        n = len(s)
        hash_value = 0
        base4 = 4

        char_to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
        nums = [char_to_int.get(char) for char in s]

        seen_pattern = set()
        result = set()

        for idx in range(n - L + 1):
            if idx == 0:
                for j in range(L):
                    hash_value = base4 * hash_value + nums[j]
            else:
                hash_value = base4 * hash_value - \
                    nums[idx - 1] * (base4 ** L) + nums[idx + L - 1]

            if hash_value in seen_pattern:
                result.add(s[idx:idx + L])
            else:
                seen_pattern.add(hash_value)

        return list(result)

# n = length of string, l = length of pattern
# Time Complexity: O((n - l) * l) ==> O(n * l)
# Space Complexity: O((n - l) * l) ==> O(n * l)
