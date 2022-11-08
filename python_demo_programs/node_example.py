class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, node):
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    # return the value for the head
    def get_first_node_value(self):
        if self.head is not None:
            return self.head.data
        return None

    def get_last_node_value(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            return current.data

    def add_last(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node


linked_list = LinkedList()
n1 = Node(1)
linked_list.add_first(n1)
n2 = Node(2)
linked_list.add_first(n2)
linked_list.add_last(Node(3))


# n1 = Node(2)
# n2 = Node(3)
#
# print(n1.data)
# print(n2.data)
#
# print(n1.next)
# n1.next = n2
# print(n1.next.data)
