class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
# """
# define append method which adds value to the end of the list
# head -> [1] -> [3] -> [2] -> X 	(5_	head -> [1] -> [3] -> [2] -> [5] -> X
# """
    def append(self,value):
        
        current_node=self.head
        while current_node !=None:
            print("looping")
        current_node=self.value
        current_node.next=None



