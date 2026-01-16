"""
Problem Number: 225. Implement Stack using Queues
Difficulty Level: Easy
Link: https://leetcode.com/problems/implement-stack-using-queues

********************************************************************************

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack
should support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:
You must use only standard operations of a queue, which means that only push to back,
peek/pop from front, size and is empty operations are valid. Depending on your language,
the queue may not be supported natively. You may simulate a queue using a list or deque
(double-ended queue) as long as you use only a queue's standard operations.

Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]
Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
Follow-up: Can you implement the stack using only one queue?
"""

from collections import deque


# Stack implementation using only one queue
class MyStack:
    def __init__(self):
        self.custom_stack = deque()

    def push(self, x: int) -> None:
        self.custom_stack.append(x)
        for _ in range(len(self.custom_stack) - 1):
            top_element = self.custom_stack.popleft()
            self.custom_stack.append(top_element)

    def pop(self) -> int:
        return self.custom_stack.popleft()

    def top(self) -> int:
        return self.custom_stack[0]

    def empty(self) -> bool:
        return len(self.custom_stack) == 0

# Time Complexity:
# push(): O(n)
# pop(): O(1)
# top(): O(1)
# emtpy(): O(1)
# Space Complexity: O(n)


# Stack implementation using only two queues
class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        length = len(self.queue1)
        for _ in range(length - 1):
            self.queue2.append(self.queue1.popleft())

        top_element = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def top(self) -> int:
        length = len(self.queue1)
        for _ in range(length - 1):
            self.queue2.append(self.queue1.popleft())

        top_element = self.queue1.popleft()
        self.queue2.append(top_element)
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def empty(self) -> bool:
        return len(self.queue1) == 0

# Time Complexity:
# push(): O(1)
# pop(): O(n)
# top(): O(n)
# emtpy(): O(1)
# Space Complexity: O(n)
