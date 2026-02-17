"""
Problem Number: 358. Rearrange String k Distance Apart
Difficulty Level: Hard
Link: https://leetcode.com/problems/rearrange-string-k-distance-apart/

********************************************************************************

Given a non-empty string s and an integer k, rearrange the string such that the
same characters are at least distance k from each other. All input strings are
given in lowercase letters. If it is not possible to rearrange the string,
return an empty string "".

Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least distance 3 from each other.

Example 2:
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.

Example 3:
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.

Constraints:
1 <= s.length <= 3 * 10^5
s consists of lowercase English letters.
0 <= k <= s.length
"""

from heapq import heappush, heappop
from collections import deque


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        count = dict()
        for char in s:
            count[char] = count.get(char, 0) + 1

        max_heap = []
        for char, freq in count.items():
            heappush(max_heap, (-freq, char))

        result = []
        queue = deque()

        while max_heap:
            curr_freq, curr_char = heappop(max_heap)
            result.append(curr_char)
            queue.append((curr_freq + 1, curr_char))

            if len(queue) >= k:
                cooled_freq, cooled_char = queue.popleft()
                if cooled_freq < 0:
                    heappush(max_heap, (cooled_freq, cooled_char))

        if len(result) != len(s):
            return ""
        return "".join(result)

# n = len(s), m = number of unique characters
# Time Complexity: O(n + (n + m) * log(m)) ==> O(n * log(m))
# Space Complexity: O(n + 3 * m) ==> O(n)
