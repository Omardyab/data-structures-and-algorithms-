
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
# """
# define insert method which adds value in head
# """
    def insert(self, value='null'):
        try:
            first_node = Node(value)
            if not self.head:
                self.head = first_node
            else:
                current_node = self.head
                self.head=first_node
                self.head.next = current_node
        except Exception as exception:
            raise Exception(f"its not working as it should be: {exception}")
# """
# define include method which check if value exisited (in this case return false) otherwise return True
# """
    def includes(self, expectedvalue):
        try:
            current_node = self.head
            while current_node:
                if current_node.value == expectedvalue:
                    return True
                    break
                current_node = current_node.next
            return False
        except Exception as exception:
                raise Exception(f"its not working as it should be: {exception}")
# """
# Visual representation of the linked list bubbles
# """
    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            value = current_node.value
            if current_node.next is None:
                result =result+ f"({value})-> None"
                break
            result = result + f"({value}) -> "
            current_node=current_node.next
        return result

    def knth_from_end(self, k_value):
        current_node = self.head
        len_list=len(self)-1
        nodes_loop=(len_list-k_value)-1
        try:
            if current_node==None:
                return ("the k value is None")
            if k_value<=-1 or k_value>len_list:
                return ("this is not a positive value or the value you have is out of the given range")
            # while nodes_loop>0:
            #     current_node = current_node.next
            #     nodes_loop=nodes_loop-1
            # print(nodes_loop)
            # return current_node.value
        except Exception as exception:
                raise Exception(f"its not working as it should be: {exception}")



if __name__ == "__main__":
    # myll=Linkedlist()
    # print("my linked list now have : ",myll)
    # myll.insert(1)
    # print("my linked list now have : ",myll)
    # myll.insert(2)
    # print("my linked list now have : ",myll)
    # myll.insert(7)
    # print("my linked list now have : ",myll)
    # myll.includes(7)
    # print("my linked list now have : ",myll)
    # myll.includes(9)
    # print("my linked list now have : ",myll)
    # print(myll)

    ll=Linkedlist()
    ll.insert(1)
    ll.insert(3)
    ll.insert(8)
    ll.insert(2)
    print(ll)
    print(ll.knth_from_end(-1))
    print(ll.knth_from_end(8))
    print(ll.knth_from_end(3))
    print(ll.knth_from_end(-44))







