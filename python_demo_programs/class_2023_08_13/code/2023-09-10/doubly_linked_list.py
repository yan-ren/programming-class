class DoublyLinkedList():
    class Node():
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.Node(None)
        self.tail.prev = self.head
        self.head.next = self.tail

    # add value in the end
    def append(self, data):
        new_node = self.Node(data)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node


    # add value in the beginning
    def prepend(self, data):
        new_node = self.Node(data)
        new_node.prev = self.head
        new_node.next = self.head.next
        self.head.next.prev = new_node
        self.head.next = new_node

    def __str__(self):
        result = ''
        current = self.head
        while current != None:
            result += str(current.data) + "->"
            current = current.next
            
        return result

    def delete(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                if current.prev != None:
                    current.prev.next = current.next
                if current.next != None:
                    current.next.prev = current.prev

    def insert_before(self, node_data, data):
        current = self.head

        while current.next != None and current.data != node_data:
            current = current.next

        if current.data == node_data:
            # insert before the current
            new_node = self.Node(data)
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node



l = DoublyLinkedList()
l.append(1)
l.append(2)
l.prepend(3)
print(l)
l.insert_before(2, 4)
print(l)
