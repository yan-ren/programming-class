'''
If you need to use Stack/Queue in python to solve any puzzle,
use python list intead

Three options:
1. Stack and queue using list
2. Stack and queue using deque library
3. Implement from scratch
'''
# option1
letters = []

# stack
letters.append('a')
letters.append('b')
letters.pop()

# queue
letters.append('c')
letters.pop(0)


# option 2
from collections import deque

numbers = deque()

# use dequeue like a stack
numbers.append(1)
numbers.pop()

# use dequeue like a queue
numbers.append(1)
numbers.popleft()

# implement a stack using singly linked list idea
class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, element):
        new_node = Node(element, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        value = self.head.element
        remove_node = self.head
        self.head = self.head.next
        remove_node.next = None

        return value


stack = LinkedStack()
stack.push(1)
stack.push(2)

print(stack.pop())