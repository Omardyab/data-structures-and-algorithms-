class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def append(self, value='null'):
        """
        Adds a node of a value to the end of LL
        """
        try:
          node = Node(value)
          if not self.head:
              self.head = node

          else:
              current = self.head
              while current.next != None:
                  current = current.next
              current.next = node
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}")
    def __init__(self):
        self.head = None
    def palindrome(ll):
        valuelist=[]
        current = ll.head
        while current:
            valuelist+=[current.value]
            current=current.next
        for i in range(len(valuelist)//2):
            if valuelist[i]!=valuelist[-1*i-1]:
                return False
        return True


if __name__ == "__main__":

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    ll.append(1)

    # ll.append(1)
    # ll.append(4)
    # print(ll.__str__())
    print(palindrome(ll))
