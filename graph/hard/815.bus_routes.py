"""
Problem Number: 815. Bus Routes
Difficulty Level: Hard
Link: https://leetcode.com/problems/bus-routes

********************************************************************************

You are given an array routes representing bus routes where routes[i] is a bus route
that the ith bus repeats forever. For example, if routes[0] = [1, 5, 7], this means that
the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever. You
will start at the bus stop source (You are not on any bus initially), and you want to go
to the bus stop target. You can travel between bus stops by buses only. Return the least
number of buses you must take to travel from source to target. Return -1 if it is not
possible.

Example 1:
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the
second bus to the bus stop 6.

Example 2:
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

Constraints:
1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5
All the values of routes[i] are unique.
sum(routes[i].length) <= 10^5
0 <= routes[i][j] < 10^6
0 <= source, target < 10^6
"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for bus_stop in route:
                stop_to_buses[bus_stop].append(bus_id)

        return self.bfs(routes, stop_to_buses, source, target)

    def bfs(self, routes: List[List[int]], stop_to_buses: dict, source: int, target: int) -> int:
        queue = deque()

        taken_buses = set()
        visited_stops = set()
        visited_stops.add(source)

        for bus_id in stop_to_buses[source]:
            queue.append(bus_id)
            taken_buses.add(bus_id)

        bus_count = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                bus_id = queue.popleft()

                for bus_stop in routes[bus_id]:
                    if bus_stop == target:
                        return bus_count

                    if bus_stop in visited_stops:
                        continue

                    visited_stops.add(bus_stop)

                    for next_bus_id in stop_to_buses[bus_stop]:
                        if next_bus_id not in taken_buses:
                            queue.append(next_bus_id)
                            taken_buses.add(next_bus_id)

            bus_count += 1

        return -1

# n = total number of bus stops across all routes
# m = total number of unique bus stops in the graph
# b = total number of buses
# Time Complexity: O(n + m)
# Space Complexity: O(n)
