class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
"""
define insert method which adds value in head
"""
    def insert(self, value='null'):
        first_node = Node(value)
        if !(self.head):
            self.head = first_node
        else:
            current = self.head
            self.head=first_node
            self.head.next = current
"""
define include method which check if value exisited (in this case return false) otherwise return True
"""
def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
                break
            current = current.next
        return False

    """
    visual representation of the linked list
    """
    def __str__(self):
        result = ""
        current = self.head
        while current:
            value = current.value
            if !(current.next):
                result += f"({value})-> None"
                break
            result = result + f"({value}) -> "
            current=current.next
        return output

if __name__ == "__main__":

    myll=Linkedlist()
    myll.insert(1)
    print(myll.__str__)







