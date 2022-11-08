from queue import Queue
import re


class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        if data < self.data:
            if self.left is None:
                self.left = BSTNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
            else:
                self.right.insert(data)

    def exist(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left is None:
                return False
            else:
                return self.left.exsit(val)
        else:
            if self.right is None:
                return False
            else:
                return self.right.exist(val)
    '''
    delete:
    case1: delete a leaf, leaf is the node with no children
    case2: delete a node with one child, 
    remove the node and replace it with its child
    case3: delete a node with two children
    '''
    # def delete(self, val):
    #     parent = None
    #     cur = self.root
    #
    #     # find the node need to be deleted
    #     while cur is not None and cur.data != val:
    #         parent = cur
    #         if val < cur.data:
    #             cur = cur.left
    #         else:
    #             cur = cur.right
    #
    #     if cur is None:
    #         return
    #
    #     # case 1: node has no children
    #     if cur.left is None and cur.right is None:
    #         if cur != self.root:
    #             if cur == parent.left:
    #                 parent.left = None
    #             else:
    #                 parent.right = None
    #         else:
    #             self.root = None
    #     # case 2: node has one child
    #     elif cur.left is not None or cur.right is not None:
    #         child = None
    #         if cur.left is not None:
    #             child = cur.left
    #         else:
    #             child = cur.right
    #         if cur != self.root:
    #             if cur == parent.left:
    #                 parent.left = child
    #             else:
    #                 parent.right = child
    #         else:
    #             self.root = child
    #     else:
    def get_minimum(self):
        cur = self.left
        while cur.left is not None:
            cur = cur.left

        return cur.data

    def get_maximum(self):
        cur = self.right
        while cur.right is not None:
            cur = cur.right

        return cur.data


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)


def preorder(node):
    if node is None:
        return

    print(node.data)
    preorder(node.left)
    preorder(node.right)


def breath_first_search(root):
    q = Queue()
    q.put(root)

    while not q.empty():
        current = q.get()
        print(current.data)
        if current.left is not None:
            q.put(current.left)
        if current.right is not None:
            q.put(current.right)


def reverse_bst(root):
    if root == None:
        return
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
    reverse_bst(root.left)
    reverse_bst(root.right)


def equal_bst(root1, root2):
    # compare the value on the root and compare if they both have left child and
    # right child
    # if one node has left where the other doesn't, they are not equal
    # if one node has right where the other doesn't, they are not equal
    if root1 == None and root2 == None:
        return True
    elif root1 == None and root2 != None:
        return False
    elif root1 != None and root2 == None:
        return False
    elif root1.data == root2.data:
        return equal_bst(root1.left, root2.left) and equal_bst(root1.right, root2.right)
    else:
        return False



# root1 = BSTNode(4)
# root1.insert(2)
# root1.insert(8)
# root1.insert(10)
# root1.insert(3)


# root2 = BSTNode(4)
# root2.insert(2)
# root2.insert(8)
# root2.insert(10)
# root2.insert(3)


# inorder(root1)
# reverse_bst(root1)
# inorder(root1)


# root2 = BSTNode(4)
# root2.insert(2)
# root2.insert(8)

'''
inorder, preorder, postorder -> depth first search

breadth first search
queue: linear datastructure, first in first out

algorithm

breadth_first(root):

initialize queue Q, add root into Q
while Q not empty:
    p = Q.remove()
    print(p.data)
    for each child of p:
        Q.add(child)
'''
def breadth_first(root):
    queue = []
    queue.append(root)

    while len(queue) != 0:
        p = queue.pop(0)
        print(p.data)
        if p.left != None:
            queue.append(p.left)
        if p.right != None:
            queue.append(p.right)


root1 = BSTNode(8)
root1.insert(3)
root1.insert(1)
root1.insert(10)
root1.insert(14)
root1.insert(6)
root1.insert(4)
root1.insert(7)
root1.insert(13)
breadth_first(root1)