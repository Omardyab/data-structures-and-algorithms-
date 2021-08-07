

"""first => Node => Create a Node class that has properties for the value stored in the Node, and a pointer to the next node"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""Stack
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created."""

class Stack:
    def __init__(self,node=None):
        self.top = None

    """The class should contain the following methods:
        push
        Arguments: value
        adds a new node with that value to the top of the stack with an O(1) Time performance."""

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
    """pop
        Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        Should raise exception when called on empty stack"""
    def pop(self):
        if self.top == None:
            raise AttributeError("Your Stack is empty with value of None")
        tempvalue = self.top
        self.top = self.top.next
        tempvalue.next=None
        return tempvalue.value
    """peek
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack"""
    def peek(self):
        if self.top == None:
            raise AttributeError("Your Stack is empty with value of None")
        return self.top.value

    """is empty
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty."""
    def isEmpty(self):
        if self.top == None:
            raise AttributeError("Your Stack is empty with value of None")
        return not self.top

"""Queue
    Create a Queue class that has a front property. It creates an empty Queue when instantiated.
    This object should be aware of a default empty value assigned to front when the queue is created."""
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    """ enqueue
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance."""
    def enqueue(self, value):
        node = Node(value)

        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node
    """peek
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack"""
    def peek(self):
        if self.front == None:
            raise AttributeError("Your Queue is empty with value of None")
        return self.front.value
    """is empty
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty"""
    def isEmpty(self):
        if self.rear:
            return False
        return True

