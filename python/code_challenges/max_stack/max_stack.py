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
        # preparing my node to be top
        node = Node(value)
        # moving top to next
        if self.top:
            node.next = self.top
        # new node on top
        self.top = node
    """pop
        Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        Should raise exception when called on empty stack"""
    def pop(self):
        # check if top is none then raise an error
        if self.top == None:
            raise AttributeError("Your Stack is empty with value of None")
        # store  top in a temp value
        tempvalue = self.top
        # reassign top to be next on ein the stack
        self.top = self.top.next

        tempvalue.next=None
        return tempvalue.value
    """peek
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack"""
    def peek(self):
        # check if top is none then raise an error
        if self.top == None:
            raise AttributeError("Your Stack is empty with value of None")
        # check what is the value of the top of the stack
        return self.top.value

    """is empty
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty."""
    def isEmpty(self):
        # check the value of top if no then return True meaning your stack is empty(not false)
        return not self.top

    def __str__(self):
        check=self.top
        stack_strrep=""
        if check:
            while(check):
                stack_strrep += f"[{ check.value }] | "
                check = check.next
        stack_strrep += "None"
        return (stack_strrep)

    def max_stack(self):
        max_value=self.top
        second_value=self.top.next
        print("your first value=",max_value.value)
        # print("your second value=",second_value.value)
        while second_value:
            if second_value.value>max_value.value:
                max_value=second_value
                second_value=second_value.next
                print("your max=",max_value.value)
            else :
                print("in else your max=",max_value.value)
                second_value=second_value.next
        return max_value.value

if __name__ == "__main__":
    stack1 = Stack()
    # top is last item which is Lucy
    stack1.push(1000)
    stack1.push(2000)
    stack1.push(3000)
    # stack1.push(2000)
    # stack1.push(000)
    print(stack1)
    print(stack1.max_stack())
    stack1.pop()
    print(stack1)
    print(stack1.max_stack())



