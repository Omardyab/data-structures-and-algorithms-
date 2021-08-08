from stack_and_queue import *
import pytest

""" Test cases for Stack
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

def test_stack_push_multiple():
    stack = Stack()
    stack.push(100)
    stack.push(200)
    assert stack.top.value == 200

def test_stack_pop():
    stack = Stack()
    stack.push(100)
    stack.push(200)
    stack.pop()
    assert stack.top.value == 100

def test_stack_empty():
    stack = Stack()
    stack.push(100)
    stack.push(200)
    stack.pop()
    stack.pop()
    assert stack.isEmpty() == True

def test_stack_peek():
    stack = Stack()
    stack.push(400)
    stack.push(600)
    assert stack.peek() == 600

# instantiate
def test_stack_instantiate():
    stack = Stack()
    assert stack.top == None

def test_stack_empty_exception():
    stack = Stack()
    with pytest.raises(Exception):
        assert stack.peek()
    with pytest.raises(Exception):
        assert stack.pop()

""" Test cases for Queue
    Can successfully enqueue into a queue
    Can successfully enqueue multiple values into a queue
    Can successfully dequeue out of a queue the expected value
    Can successfully peek into a queue, seeing the expected value
    Can successfully empty a queue after multiple dequeues
    Can successfully instantiate an empty queue
    Calling dequeue or peek on empty queue raises exception """
def test_enqueue_one():
    queue = Queue()
    queue.enqueue(700)
    assert queue.rear.value == 700

def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue(700)
    queue.enqueue(800)
    assert queue.rear.value == 800
    assert queue.front.value == 700

def test_dequeue():
    queue = Queue()
    queue.enqueue(700)
    queue.dequeue()
    queue.enqueue(800)
    assert queue.front.value == 800

def test_queue_peek():
    queue = Queue()
    queue.enqueue("Omar")
    queue.enqueue("Nawras")
    assert queue.peek() == "Omar"

def test_is_empty():
    queue = Queue()
    queue.enqueue("Omar")
    queue.enqueue("Nawras")
    queue.dequeue()
    queue.dequeue()
    assert queue.isEmpty() == True

def test_instantiate():
    queue = Queue()
    assert queue.front == None
    assert queue.rear == None

def test_queue_empty_exception():
    queue = Queue()
    with pytest.raises(Exception):
        assert queue.peek()
    with pytest.raises(Exception):
        assert queue.dequeue()
