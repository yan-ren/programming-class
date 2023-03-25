<H1>
Data structure review/new concept
</H1>

<H2>
Stack/Queue ADT

ADT: Abstract Data Structure, theoretical data structure, without fixed implementation
Only the property is defined, implementation is flexible


Python dictionary/set/list: concrete data structure with fixed implementation in Python

Stack: A stack is a collection of objects that are inserted and removed according to the last-in, 
first-out principle

Queue: A queue is a collection of object that are inserted and removed according to the first-in, first out principle

What about Stack/Queue in Python?

stack, even though python does not have implemented class for stack, but we can easily build a stack using python list

queue, python does have a class called dequeue, which is the python implementation for Queue, but we can still build queue using python list

Overall, both stack and queue can be implemented using python list
</H2>

<H3>
Example about using stack to solve problem

next greater element

Given a list of values, for each value x, find the first greater element that is to the right of x in the list. If there is no greater value, put -1

[4, 5, 2, 25]

[5, 25, 25, -1]

create an empty stack S

create a list to store the output

for each element in input list

if the value is smaller than the top value of the stack, we push the value to the stack
otherwise, pop element from stack till the top of stack is smaller than the current element or the stack becomes empty

</H3>








