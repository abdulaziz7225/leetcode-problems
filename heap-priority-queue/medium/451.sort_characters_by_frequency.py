"""
Problem Number: 451. Sort Characters By Frequency
Difficulty Level: Medium
Link: https://leetcode.com/problems/sort-characters-by-frequency/

********************************************************************************

Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string. Return the
sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.
"""

from heapq import heappush, heappop


# Solution 1: Sorting
class Solution:
    def frequencySort(self, string: str) -> str:
        result = []
        counter = dict()

        for char in string:
            counter[char] = counter.get(char, 0) + 1

        sorted_pairs = sorted(
            counter.items(), key=lambda x: x[1], reverse=True)
        for char, freq in sorted_pairs:
            result.append(char * freq)

        return "".join(result)

# m is the number of unique characters
# Time Complexity: O(2 * n + m * log(m)) ==> O(n + m * log(m))
# Space Complexity: O(n + 2 * m) ==> O(n + m)


# Solution 2: Heap Priority Queue
class Solution:
    def frequencySort(self, string: str) -> str:
        result = []
        counter = dict()

        for char in string:
            counter[char] = counter.get(char, 0) + 1

        max_heap = []
        for char, freq in counter.items():
            heappush(max_heap, [-freq, char])

        while max_heap:
            freq, char = heappop(max_heap)
            result.append(char * -freq)

        return "".join(result)

# m is the number of unique characters
# Time Complexity: O(2 * n + 2 * m * log(m)) ==> O(n + m * log(m))
# Space Complexity: O(n + 2 * m) ==> O(n + m)


# Solution 3: Bucket Sort
class Solution:
    def frequencySort(self, string: str) -> str:
        result = []
        counter = dict()

        for char in string:
            counter[char] = counter.get(char, 0) + 1

        max_freq = max(counter.values())
        freq_bucket = [[] for _ in range(max_freq)]

        for char, freq in counter.items():
            freq_bucket[freq - 1].append(char)

        for i in range(len(freq_bucket) - 1, -1, -1):
            for char in freq_bucket[i]:
                result.append(char * (i + 1))

        return "".join(result)

# m is the number of unique characters
# Time Complexity: O(2 * (n + m) + max_freq) ==> O(n + m)
# Space Complexity: O(2 * n + m) ==> O(n + m)
