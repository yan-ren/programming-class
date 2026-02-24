'''
LRUCache cache = new LRUCache(2);  // capacity = 2

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
from wsgiref.validate import header_re


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node(0, 0) # create a dummy node for head, skip None checking when adding the first node
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {} # key -> node

    # help function
    # add head
    def _add_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # remove any given node from the list
    def _delete(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        # dereference the node from the list
        node.prev = None
        node.next = None

    def print(self):
        current = self.head

        while current is not None:
            print(current.value, '->', end='')
            current = current.next

        print()

    # put
    # if exists, update the value and move it to the head (remove, and add to the head)
    # if doesn't, try to add to head by checking the capacity,
    #       if full, remove the node on the tail, and insert in the head
    #       otherwise, just add to the head
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._delete(node)
            self._add_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_head(node)

            if len(self.cache) > self.capacity:
                del self.cache[self.tail.prev.key]
                self._delete(self.tail.prev)

    def get(self, key):
        if key not in self.cache:
            return -1
        current = self.cache[key]
        self._delete(current)
        self._add_head(current)
        return current.value

# cache = LRUCache(4)
# n1 = Node(2, 2)
# n2 = Node(3, 3)
# cache._add_head(n1)
# cache._add_head(n2)
# cache.print()
#
# cache._delete(n1)
# cache.print()

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.print()
print(cache.get(1)) # return 1
cache.print()
cache.put(3, 3) # remove key 2
cache.print()
print(cache.get(2)  )              # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
cache.print()
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4

















