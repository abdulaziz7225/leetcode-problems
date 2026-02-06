"""
Problem Number: 2502. Design Memory Allocator
Difficulty Level: Medium
Link: https://leetcode.com/problems/design-memory-allocator

********************************************************************************

You are given an integer n representing the size of a 0-indexed memory array. All memory
units are initially free. You have a memory allocator with the following
functionalities: Allocate a block of size consecutive free memory units and assign it
the id mID. Free all memory units with the given id mID.
Note that:
Multiple blocks can be allocated to the same mID. You should free all the memory units
with mID, even if they were allocated in different blocks.
Implement the Allocator class:
Allocator(int n) Initializes an Allocator object with a memory array of size n.
int allocate(int size, int mID) Find the leftmost block of size consecutive free memory
units and allocate it with the id mID. Return the block's first index. If such a block
does not exist, return -1.
int freeMemory(int mID) Free all memory units with the id mID. Return the number of
memory units you have freed.

Example 1:
Input
["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate",
"allocate", "freeMemory", "allocate", "freeMemory"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
Output
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]
Explanation
Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory
units are initially free.
loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes
[1,_,_,_,_,_,_,_,_,_]. We return 0.
loc.allocate(1, 2); // The leftmost block's first index is 1. The memory array becomes
[1,2,_,_,_,_,_,_,_,_]. We return 1.
loc.allocate(1, 3); // The leftmost block's first index is 2. The memory array becomes
[1,2,3,_,_,_,_,_,_,_]. We return 2.
loc.freeMemory(2); // Free all memory units with mID 2. The memory array becomes [1,_,
3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
loc.allocate(3, 4); // The leftmost block's first index is 3. The memory array becomes
[1,_,3,4,4,4,_,_,_,_]. We return 3.
loc.allocate(1, 1); // The leftmost block's first index is 1. The memory array becomes
[1,1,3,4,4,4,_,_,_,_]. We return 1.
loc.allocate(1, 1); // The leftmost block's first index is 6. The memory array becomes
[1,1,3,4,4,4,1,_,_,_]. We return 6.
loc.freeMemory(1); // Free all memory units with mID 1. The memory array becomes
[_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
loc.allocate(10, 2); // We can not find any free block with 10 consecutive free memory
units, so we return -1.
loc.freeMemory(7); // Free all memory units with mID 7. The memory array remains the
same since there is no memory unit with mID 7. We return 0.

Constraints:
1 <= n, size, mID <= 1000
At most 1000 calls will be made to allocate and freeMemory.
"""

from collections import defaultdict
from sortedcontainers import SortedDict


class Allocator:
    def __init__(self, n: int):
        # Maps mID to a list of allocated blocks (addr, size)
        self.allocations = defaultdict(list)
        # Maps address to block size, ordered by address automatically
        self.free_blocks = SortedDict({0: n})

    def _add_and_merge(self, addr: int, size: int) -> None:
        # Insert the new free block and get its iterator
        self.free_blocks[addr] = size

        index = self.free_blocks.index(addr)

        if index + 1 < len(self.free_blocks):
            next_addr = self.free_blocks.iloc[index + 1]
            if addr + size == next_addr:
                # Extend current block
                self.free_blocks[addr] += self.free_blocks[next_addr]
                # Remove right neighbor
                del self.free_blocks[next_addr]

        # 2. Try to merge with the PREVIOUS block (Left Neighbor)
        if index > 0:
            prev_addr = self.free_blocks.iloc[index - 1]
            prev_size = self.free_blocks[prev_addr]
            if prev_addr + prev_size == addr:
                # Extend left neighbor
                self.free_blocks[prev_addr] += self.free_blocks[addr]
                # Remove current block
                del self.free_blocks[addr]

    def allocate(self, size: int, mID: int) -> int:
        # Iterate linearly to find the first fit
        for addr, capacity in self.free_blocks.items():

            if capacity >= size:
                # Record the allocation
                self.allocations[mID].append((addr, size))
                # Remove the original free block
                del self.free_blocks[addr]
                # If there is leftover space, add it back as a new free block
                if capacity > size:
                    self.free_blocks[addr + size] = capacity - size

                return addr

        return -1

    def freeMemory(self, mID: int) -> int:
        if mID not in self.allocations:
            return 0

        freed_size = 0

        # Process all blocks owned by this mID
        for addr, size in self.allocations[mID]:
            self._add_and_merge(addr, size)
            freed_size += size

        # Remove the record of this mID entirely
        del self.allocations[mID]

        return freed_size


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)

# n = number of disjoint free memory blocks (entries in available)
# k = number of blocks currently held by the specific mID being freed
# b = total number of allocated blocks (entries in alloc)
# Time Complexity:
# allocate(): O(n)
# freeMemory(): O(k * log(n))
# Space Complexity: O(n + b)
