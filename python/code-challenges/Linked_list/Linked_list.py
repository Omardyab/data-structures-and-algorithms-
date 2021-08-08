
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
    """This is for code ch 7, two functions one to mesure the length of the list and one to get the knth_from_end """
    def length_list_nodes(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.length_list_nodes(node.next)

    def knth_from_end(self, k_value):
        current_node = self.head
        len_list=self.length_list_nodes(current_node)-1
        # print("original list length",len_list)
        # print("the length of my list is",len_list)
        try:
            if current_node==None:
                return ("the k value is None")
            elif k_value<0:
                return ("This is not a positive value")
            elif k_value>len_list:
                return ("Out of the given range")

            else:
                idx=(len_list)-k_value
                count=0
                # print("your index",idx)
                while current_node:
                    # print("is ",len_list,"==",idx)
                    if count==idx:
                        # print("the length in while loop",len_list,"value of my node", current_node.value)
                        return(current_node.value)
                    count=count+1
                    current_node=current_node.next
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


    """this is for code ch 7"""
    ll=Linkedlist()
    ll.insert(1)
    ll.insert(3)
    ll.insert(8)
    ll.insert(2)
    print(ll)
    # 2 -> 8 ->3-> 1
    print(ll.knth_from_end(-1))
    print(ll.knth_from_end(8))
    print(ll.knth_from_end(0))
    print(ll.knth_from_end(1))
    print(ll.knth_from_end(3))
    print(ll.knth_from_end(4))
    ll2=Linkedlist()
    ll2.insert(5)
    ll2.insert(6)
    ll2.insert(7)

    print(ll2)
    # 7 -> 6 ->5-> None
    # print(ll2.knth_from_end(-4))
    # print(ll2.knth_from_end(4))
    print(ll2.knth_from_end(-2))
    print(ll2.knth_from_end(1))
    print(ll2.knth_from_end(0))
    print(ll2.knth_from_end(3))








