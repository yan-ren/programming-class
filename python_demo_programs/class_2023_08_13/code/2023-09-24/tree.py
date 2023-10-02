class Tree:
    '''Base class for a tree structure'''
    def root(self):
        '''return Poisition representing the tree's root'''
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, node):
        '''return Position representing p's parent'''
        raise NotImplementedError('must be implemented by subclass')

    def children(self, node):
        '''generate an iterator of Positions reperenting p's children'''
        raise NotImplementedError('must be implemented by subclass')


class LinkedBinaryTree(Tree):
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
    # binary tree constructor
    def __init__(self):
        self._root = None
        self._size = 0

    # binary tree public method
    def add_root(self, element):
        if self._root is not None:
            raise ValueError('Root exists')

        self._size = 1
        self._root = self._Node(element)

    def add_left(self, parent_node, element):
        self._size += 1
        parent_node._left = self._Node(element, parent_node)

    def add_right(self, parent_node, element):
        self._size += 1
        parent_node._right = self._Node(element, parent_node)

    def delete(self, node):
        '''
        delete the node and replace it with its child

        if node has two children, rains error
        '''
        if node._left is not None and node._right is not None:
            raise ValueError('node has two children')
        
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent # child's grandparnet becomes parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = None

        return node._element