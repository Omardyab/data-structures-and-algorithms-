
# import pytest
# from Linked_list import *
# # from Linked_list import __version__

# # def test_version():
# #     assert __version__ == '0.1.0'
# def test_empty_l_list():
#     emptylist=Linkedlist()
#     actual=emptylist
#     expected=''
#     assert actual==expected


# def test_insert():
#     myll = Linkedlist()
#     myll.insert(12)
#     actual =myll.head.value
#     expected=12
#     assert actual==expected

# def test_linked_states(myll):
#     assert str(myll) == f"(6) -> (54) -> (100)-> None"

# def test_includes(myll):
#     assert myll.includes(50) == False
#     assert myll.includes(100) == True

# def test_head_node(myll):
#     assert myll.head.value == 6
#     assert myll.head.next.value == 54


# @pytest.fixture

# def myll():
#     llist=Linkedlist()
#     llist.insert(100)
#     llist.insert(54)
#     llist.insert(6)
#     return llist


#     """ code ch 7 tests"""
# def knth_from_end():
#     ll=Linkedlist()
#     ll.insert(1)
#     ll.insert(3)
#     ll.insert(8)
#     ll.insert(2)
#     assert ll.knth_from_end(-1)=="This is not a positive value"
#     assert ll.knth_from_end(8)=="The value you have is out of the given range"
#     assert ll.knth_from_end(0)==1
#     assert ll.knth_from_end(1)==3



# testing code ch 5 linkdist
import pytest

from linked_list.linked_list import *
# from linked_list.linked_list import *

from Linked_list import *

# from Linked_list import __version__

def test_empty_l_list():
    emptylist=Linkedlist()
    actual=emptylist
    assert actual==None
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


# testing code ch 6 linkdistinsertion
def test_append():
    myll3=Linkedlist()
    myll3.append(20)
    assert myll3.head.value==20
    # actual2= myll3.append('30')
    # assert actual2.head.next.next==None
def test_insert_before():
    myll4=Linkedlist()
    myll4.append(44)
    myll4.append(66)
    myll4.insert_before(66,55)
    assert myll4.head.next.value==55


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



