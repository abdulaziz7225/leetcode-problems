# Solving Data Structure and Algorithm Problems on LeetCode Using Python

This repository contains solutions to various data structure and algorithm problems from [LeetCode](https://leetcode.com/). All solutions are implemented in **Python** and are structured for easy understanding and reusability.

---

## Repository Structure

- Each solution is stored in a separate Python file, named according to the problem number and title.
- Solutions are organized into categories based on the problem type, such as Arrays, Strings, Trees, Graphs, etc.

### Directory Layout

```
.
├── Array
│   ├── 1.two-sum.py
│   ├── 1464.maximum-product-of-two-elements-in-an-array.py
│   ├── 35.search-insert-position.py
│   └── 48.rotate-image.py
├── Hash_Table
│   └── 1930.unique-length-3-palindromic-subsequences.py
├── Linked_List
│   ├── 206.reverse-linked-list.py
│   ├── 82.remove-duplicates-from-sorted-list-ii.py
│   ├── 83.remove-duplicates-from-sorted-list.py
│   └── 876.middle-of-the-linked-list.py
├── Prefix_Sum
│   ├── 1769.minimum-number-of-operations-to-move-all-balls-to-each-box.py
│   ├── 2270.number-of-ways-to-split-array.py
│   ├── 2381.shifting-letters-ii.py
│   └── 2559.count-vowel-strings-in-ranges.py
├── String
│   └── 1422.maximum-score-after-splitting-a-string.py
├── README.md
├── directory_layout_script.py
└── problem_description_script.py
```

---

## Problem Categories

- **Arrays**: Solutions to problems involving arrays, such as searching, sorting, and subarray sums.
- **Strings**: Problems focusing on string manipulations, substrings, and pattern matching.
- **Linked Lists**: Challenges dealing with singly and doubly linked lists.
- **Trees**: Binary trees, binary search trees, and n-ary trees.
- **Graphs**: Graph traversal, shortest path, and connectivity.
- **Dynamic Programming**: Problems requiring optimal substructure and overlapping subproblems.

---

## Solution Format

Each solution file contains:

1. **Problem Description**: A detailed explanation of the problem, its constraints, and examples.
2. **Test Cases**: Example inputs and expected outputs.
3. **Python Implementation**: The function or class implementing the solution.
4. **Time and Space Complexity Analysis**: A brief analysis of the efficiency of the solution.

Example:

```python
"""
Problem Number: 1. Two Sum
Difficulty Level: Easy
https://leetcode.com/problems/two-sum/

********************************************************************************

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = dict()
        for idx, num in enumerate(nums):
            if target - num in pairs:
                return [pairs[target - num], idx]
            pairs[num] = idx

# Time Complexity: O(n)
# Space Complexity: O(n)
```
