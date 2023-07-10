<H1>
Abstract data structure

Is data structure whose behavior/property is defined. But no fixed implementation

common path to study this topic is 
1. learn the ADT property
2. Try to implement in a language


</H1>

<H2>
Stack

Linear data structure (List), one property: LIFO (Last In First Out)

If you write Stack from scratch (class Stack)
- push(e): adds element to the top of the stack
- pop(): removes and returns the top element from the stack. edge case: if stack is empty?
- peak(): return the top element of the stack without removing it
- size(): return the number of elements in the stack
- isEmpty()


Classic question:
Given a string containing open and close braces, check if it's represents a balanced expression


e.g balanced
[ ] ( ) { }

{ { } }

{ [ { } { } ] } [ ( ) ]

not balanced
{ ( )[ } ]

( { ) }

algorithm using stack:
- loop through the string, if the current char is the open brace [ ( {, push it into the stack
- if the current char is close brace ] ) }, pop a char from the stack, if the poped char is not the same as the current, return false, otherwise continue.
- if the loop is done, and stack is empty, then all brace are in pair, otherwise, some braces don't have pair, return false
</H2>


Find next greater element for every element in an array

Given an array, find the next greater elemetn for every element, The next greater element for an element is the first greater element on the right side of the array, if element does have greater element on its right, set -1

Input
[3, 2, 8, 7, 9, 17, 12]

[8, 8, 9, 9, 17, -1, -1]


Output
[8, 8, 9, 9, 17, -1, -1]

create an empty stack S

loop through array, push value to stack if this value is smaller than the top of stack

if current value is greater than top of stack, pop from stack until the top of stack is smaller that current value.


<H2>
Queue

Linear data structure, very similiar as Stack, but it's first in first out (FIFO)
</H2>

Real world example: call centre

Graph algorithm -> Breath First Search -> Queue

Queue as ADT operations:
- enqueue(e): adds element e to the queue
- dequeue() : remove and return the first value from the queue
- first() : return the first element of queue
- size(): return the number of elements in the queue
- isEmpty(): 

Queue in Java library
- Interface
- LinkedList (or PriorityQueue)

Example question:

Number of islands
Given an mxn 2D array grid, 1 represent land, 0 represent water, return the number of islands

A land is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

grid = [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1]
]

Another Queue

Double-Ended Queue:

Double-Ended Queue is a queue-like data structure that supports insertion and deletion at both the front and the back of the queue

Circular Queue

It supports all queue operation with additional: rotate mehtod

rotate: move the first element to the end of the queue

LinkedList


Tree

General Tree

The elements inside tree are origanized in hierachy

A tree is an ADT that stores elements hierarchically

Formal Tree Definition

define a tree T as a set of nodes storing elements such that the nodes have a parent child reslationship

The nodes have to satisfy the following properties:

- The top node is called root node, which has no parent
- Each node has a unique parent node

Each node

Binary Tree

Properties:
- each nodes has at most two children
- each child node is labeled as left child or right child

Height: the height of a tree is the maximum of the depths of its leaf, 
in other word, height is the number of edges on the longest path from the node to leaf

Depth: the depth of a node is the number of edges from the node to the root node

In terms of a tree: the height of a tree is the height of root node == depth of its deepest node

How to implement Tree

Tree Algorithm

Binary Search Tree

Base on Binary Tree with following properties:
1. value stored in the left subtree of node are less than the value in the node
2. value stored in the right subtree of node are bigger than the value in the node

#### Binary Search Tree Insertion:

#### Binary Search Tree Search:
- value found
- value not exists

#### Tree Travesal

A traversal of a tree is a systematic way of visiting all nodes in a tree

- depth-first
  - preorder
    - the root of tree is visted first and then the left subtree and then the right subtree.
  - postorder
    - left, right, root 
  - inorder
    - left, root, right

- breadth-first
  - queue

- Deletion: assume we are deleting node x, node x can have following cases
  - if at most one of the children of node x is internal
  - if node x has two children

#### Priority Queue
- Compare to the Queue: priority queue arranges the elements base on priority. 
- ADT
- can be implemented using array, linked list or heap
- binary heap: ADT, complete binary tree
  - binary heap is a binary tree, with two properties: 1. The heap has to be complete binary tree. 2. for any node p, the key stored at p is greater than or equal to the key stored at p's parent