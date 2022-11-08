class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, value):
        node = Node(value)
        # when adding the first node
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    # print all the values in the nodes
    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def add_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def remove(self, value):
        # when the linked list is empty
        if self.head is None:
            return

        # when the head is the node need to be removed
        if self.head.value == value:
            current = self.head
            self.head = self.head.next
            current.next = None
            return

        # loop through the linked list find the node to remove
        previous = self.head
        current = self.head
        while current is not None:
            if current.value == value:
                previous.next = current.next
                current.next = None
                return
            previous = current
            current = current.next


linked_list = LinkedList()
linked_list.add_first(2)
linked_list.add_first(3)
linked_list.add_end(4)
linked_list.print()
linked_list.remove(4)
linked_list.print()

