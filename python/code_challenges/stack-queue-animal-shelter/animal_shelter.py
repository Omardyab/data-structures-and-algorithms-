
class Node:
    def __init__(self,name,next=None):
        self.name=name
        self.next=next
class Dog:
    def __init__(self, name):
        self.name=name
        self.next=None
        self.kind='dog'
class Cat:
    def __init__(self, name):
        self.name=name
        self.next=None
        self.kind='cat'
class AnimalShelter:

    def __init__(self):
        self.front= None
        self.rear = None
    """ enqueue
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance."""
    def enqueue(self, value):
        node = Node(value)
       # rear node would point to new node and rear would alos be new node
        if self.rear:
            self.rear.next = node
            self.rear = node
        # otherwise the node would be both rear and front
        else:
            self.rear=self.front = node

    """is empty
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty"""
    def isEmpty(self):
        # either ways are correct
        # first one
        if self.rear:
            return False
        return True
        # second method
        # return not self.rear
    """dequeue
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        """
    def dequeue(self,pref=None):
        curr_node=self.front
        curr_next=self.front
        deq_value=None
        # move the front to the next value and remove the current one , but first if we have one value then it will be none
        if self.front == None:
            raise AttributeError("Your shelter is empty with no animals")
        if pref != "cat" and pref !="dog":
           return "null"
        if not pref:
            temp=curr_node
            curr_node=curr_next
            return temp.value
        while curr_next:
                if curr_next.name==pref:
                    print("inside while cond")
                    curr_next=curr_next.next
                    deq_value=curr_next.name
                    break
                else:
                    curr_node=curr_next
                    curr_next=curr_next.next
        if self.front:
            self.rear=None
        return deq_value

    def __str__(self):
        check=self.front
        queue_strrep=""
        if check:
            while(check):
                queue_strrep += f"[{ check.name }] <= "
                check = check.next
        queue_strrep += "None"
        return queue_strrep

if __name__ == "__main__":

    animal_queue = AnimalShelter()
    animal_queue.enqueue(Cat('Lucy'))
    animal_queue.enqueue(Dog('Husky'))
    animal_queue.enqueue(Cat('Tiger'))
    animal_queue.enqueue(Dog('Kitty'))
    print(animal_queue)
    animal_queue.dequeue('cat')
    print(animal_queue)
    animal_queue.dequeue('dog')
    print(animal_queue)
    animal_queue.dequeue()
    print(animal_queue)
