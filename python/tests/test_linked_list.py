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


    # code ch 10 tests


