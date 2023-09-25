class Tree:
    '''Base class for a tree structure'''
    class Position:
        '''Base class represents the location of a single element'''
        def element(self):
            '''Return the element stored at this Position'''
            raise NotImplementedError('must be implemented by subclass')
        
    def root(self):
        '''return Poisition representing the tree's root'''
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        '''return Position representing p's parent'''
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        '''generate an iterator of Positions reperenting p's children'''
        raise NotImplementedError('must be implemented by subclass')


class BinaryTree(Tree):
    