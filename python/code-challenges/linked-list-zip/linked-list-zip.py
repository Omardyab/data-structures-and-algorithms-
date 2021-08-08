
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
    """
    define append method which adds value to the end of the list
    head -> [1] -> [3] -> [2] -> X 	(5_	head -> [1] -> [3] -> [2] -> [5] -> X
    """
    def append(self,value="None"):
        current_node=Node(value)
        if not self.head:
            self.head=current_node
        else:
            current=self.head
            while current.next !=None:
                print(current.value)
                # print("looping")
                current=current.next
        current.next=current_node
        #     while current_node !=None:
        #         print(current_node.value)
        #         print("looping")
        #         current_node=current_node.next
        # if current_node ==None:
        #     print("its none")
        #     current_node=self.value
        #     current_node.next=None
    """
    define inset_before method which adds value before specific node
    head -> [1] -> [3] -> [2] -> X	(3, 5)	head -> [1] -> [5] -> [3] -> [2] -> X
    """
    def insert_before(self,first,second):
        head_node=self.head
        current_node=Node(second)
        if head_node.value==first:
             current_node.next = self.head
             self.head = head_node
        else:
            while head_node:
                if head_node.next.value==first:
                    current_node.next=head_node.next
                    head_node.next=current_node
                    break
                head_node=head_node.next

    def insert_after(self,first,second):
        head_node=self.head
        new_node=Node(second)
        while head_node:
            if head_node.value==first:
                next_head=head_node.next
                head_node.next=new_node
                head_node.next.next=next_head
                break
            head_node=head_node.next

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
    def insert_after(self,first,second):
        head_node=self.head
        new_node=Node(second)
        while head_node:
            if head_node.value==first:
                next_head=head_node.next
                head_node.next=new_node
                head_node.next.next=next_head
                break
            head_node=head_node.next

    """code ch 8 linked_list_zip """
    def linked_list_zip(self,f_list,s_list):
        f_list=f_list.head
        s_list=s_list.head
        print("first value ",f_list.value)
        print("second value ",s_list.value)
        while f_list !=None:
            # print(first_list.next.value)
            saved_value=f_list.next.value
            saved_value_2=f_list.next.next.value
            print("your saved value",saved_value)
            print("your saved value",saved_value_2)
            # print(type(saved_value))
            f_list.next.value=s_list.value
            f_list.next.next=saved_value
            # print("taken value",f_list.next.value)
            print(f_list.value)
            s_list=s_list.next
            f_list=f_list.next


    def pal(self,pal_list):
        mylist=[]
        if pal_list== None:
            return False
        if pal_list.length_list_nodes==1:
            if pal_list.next.value==None:
                return False
        current_node = pal_list.head
        while current_node:
            mylist+=[current_node.value]
            print("current value",mylist)
            current_node=current_node.next
            # print(current_node.value)
        for i in range(len(mylist)//2):
            if mylist[i]!=mylist[-1*i-1]:
                return False
            # print("first list",mylist[i])
            # print("2nd ",mylist[-1*i-1])
        return True


# if __name__ == "__main__":

#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(2)
#     ll.append(1)

#     # ll.append(1)
#     # ll.append(4)
#     # print(ll.__str__())
#     print(palindrome(ll))

# // call it on a instance of that class
myfl=Linkedlist()
myfl.insert("t")
myfl.insert("o")
myfl.insert("t")
# myfl.insert(2)
# myfl.insert(3)
# myfl.insert(1)
print(myfl)
# myfl.insert_after(3,3)
print(myfl.pal(myfl))
# print(my2l)
# print(pal(myfl))
my2l=Linkedlist()
my2l.insert(1)
# my2l.insert(3)
# my2l.insert(2)
# my2l.insert(2)
# my2l.insert(3)
# my2l.insert(1)
print(my2l)
# myfl.insert_after(3,3)
print(my2l.pal(my2l))

# interview with Nura link :https://docs.google.com/spreadsheets/d/13jw2ZSK6Q9mUuiLgoP3DKosEhRicc7FFkOxseWRlqn8/edit#gid=0
