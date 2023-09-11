'''
If you need to use Stack/Queue in python to solve any puzzle,
use python list intead

Three options:
1. Stack and Queue using List
2. Stack and Queue using deque library
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

# print(stack.pop())

class LinkedQueue:

    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add value to tail
    def add(self, value):
        new_node = Node(value, Node)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    # remove from the head
    def remove(self):
        if self.size == 0:
            raise Exception('Queue is empty')
        
        value = self.head.element
        removed = self.head
        self.head = self.head.next
        removed.next = None
        self.size -= 1

        if self.size == 0:
            self.tail = None

        return value
    
queue = LinkedQueue()
queue.add(1)
queue.add(2)
queue.add(3)

print(queue.remove())
print(queue.remove())