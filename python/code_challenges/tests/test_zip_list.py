import pytest
from linked_list_zip.linked_list_zip import *

def test_zipLists_second_longer():
    myfl=Linkedlist()
    myfl.insert(2)
    myfl.insert(3)
    myfl.insert(1)
    # myfl.insert_after(3,3)
    print(myfl)
    my2l=Linkedlist()
    my2l.insert(4)
    my2l.insert(9)
    my2l.insert(5)
    print(my2l)
    actual=linked_list_zip(myfl,my2l)
    assert actual=="(1) -> (5) -> (3) -> (9)-> (2)-> (4)-> None"
