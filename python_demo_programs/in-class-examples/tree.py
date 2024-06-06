class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def insert_iterative(root, value):
    cur = root
    previous = None

    while (cur != None):
        previous = cur
        if cur.num > value:
            cur = cur.left
        else:
            cur = cur.right

    if value < previous.value:
        previous.left = Node(value)
    else:
        previous.right = Node(value)


def insert_recursive(root, value):
    if root is None:
        return Node(value)
    
    if root.value < value:
        root.right = insert_recursive(root.right, value)
    else:
        root.left = insert_recursive(root.left, value)

    return root


root = Node(4)
insert_iterative(root, 8)
insert_iterative(root, 5)
insert_iterative(root, 1)


def inorder(node):
    if node == None:
        return

    inorder(node.left)
    print(node.num)
    inorder(node.right)


inorder(root)

def preorder(node):
    if node == None:
        return
    
    print(node.num)
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if node == None:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node.num)
'''
binary search tree traversal
- depth first search traverse
 - preorder: node itself, left child, right child
 - inorder: left child, node itself, right child
 - postorder: left child, right child, node itself
- breadth first search

'''