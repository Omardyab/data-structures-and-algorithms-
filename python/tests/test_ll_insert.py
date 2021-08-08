# import pytest
from   code_challenges.ll_insert.ll_insert import *

""" Can successfully add a node to the end of the linked list
    Can successfully add multiple nodes to the end of a linked list
    Can successfully insert a node before a node located i the middle of a linked list
    Can successfully insert a node before the first node of a linked list
    Can successfully insert after a node in the middle of the linked list
    Can successfully insert a node after the last node of the linked list"""

def test_append_empty():
    mylist = Linkedlist()
    mylist.append(100)
    actual=mylist.head.value
    assert actual == 100

def test_append():
     mylist = Linkedlist()
     mylist.insert("A")
     mylist.insert("B")
     mylist.append("C")
     actual=mylist.head.next.next.value
     assert actual == "C"

def test_append_multiple():
    mylist = Linkedlist()
    mylist.append("A")
    mylist.append("B")
    mylist.append("C")
    assert mylist.head.value == "A"
    assert mylist.head.next.value == "B"
    assert mylist.head.next.next.value == "C"

def test_insert_before_mid_node():
    mylist = Linkedlist()
    mylist.append("A")
    mylist.append("B")
    mylist.append("C")
    mylist.insertBefore("B", "E")
    assert mylist.head.next.value == "E"

def test_insert_before_first_node():
    mylist = Linkedlist()
    mylist.append("A")
    mylist.append("B")
    mylist.append("C")
    mylist.insertBefore("B", "E")
    assert mylist.head.next.value == "E"

def test_insert_after_mid_node():
    mylist = Linkedlist()
    mylist.append(100)
    mylist.append(300)
    mylist.append(400)
    mylist.insertAfter(300, 200)
    assert mylist.head.next.next.value == 200

def test_insert_after_last():
    mylist = Linkedlist()
    mylist.append(100)
    mylist.append(200)
    mylist.append(400)
    mylist.insertAfter(400, 500)
    assert mylist.head.next.next.value == 500



# def test_head_node(myll):
#     assert myll.head.value == 6
#     assert myll.head.next.value == 54
# def test_falsy_values():
#     myll2=Linkedlist()
#     myll2.insert('12')
#     myll2.insert('212')
#     actual=myll2.includes('2121')
#     assert actual==False

# @pytest.fixture
# def myll():
#     llist=Linkedlist()
#     llist.insert(100)
#     llist.insert(54)
#     llist.insert(6)
#     return llist

# # testing code ch 6 linkdistinsertion
# def test_append():
#     myll3=Linkedlist()
#     myll3.append(20)
#     assert myll3.head.value==20
#     # actual2= myll3.append('30')
#     # assert actual2.head.next.next==None
# def test_insert_before():
#     myll4=Linkedlist()
#     myll4.append(44)
#     myll4.append(66)
#     myll4.insert_before(66,55)
#     assert myll4.head.next.value==55

