import pytest
from Linked_list import *
# from Linked_list import __version__

# def test_version():
#     assert __version__ == '0.1.0'
def test_empty_l_list():
    emptylist=Linkedlist().head
    actual=emptylist
    expected=None
    assert actual==expected

def test_insert():
    myll = Linkedlist()
    myll.insert(12)
    actual =myll.head.value
    actualnext=myll.head.next
    expected=12
    expectednext=None
    assert actual==expected
    assert actualnext==expectednext

def test_linked_states(myll):
    assert str(myll) == f"(6) -> (54) -> (100)-> None"

def test_includes(myll):
    assert myll.includes(50) == False
    assert myll.includes(100) == True

def test_head_node(myll):
    assert myll.head.value == 6
    assert myll.head.next.value == 54
def test_falsy_values():
    myll2=Linkedlist()
    myll2.insert('12')
    myll2.insert('212')
    actual=myll2.includes('2121')
    assert actual==False

@pytest.fixture
def myll():
    llist=Linkedlist()
    llist.insert(100)
    llist.insert(54)
    llist.insert(6)
    return llist
