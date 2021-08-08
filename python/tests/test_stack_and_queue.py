from stack_and_queue import *
import pytest

"""Write tests to prove the following functionality:
    Can successfully push onto a stack
    Can successfully push multiple values onto a stack
    Can successfully pop off the stack
    Can successfully empty a stack after multiple pops
    Can successfully peek the next item on the stack
    Can successfully instantiate an empty stack
    Calling pop or peek on empty stack raises exception"""
def test_stack_push_one():
    stack = Stack()
    stack.push(100)
    assert stack.top.value == 100
