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

    def enqueue(self, value):
            # node = Node(value)
        # rear node would point to new node and rear would alos be new node
            if self.rear:
                self.rear.next = value
                self.rear = value
            # otherwise the node would be both rear and front
            else:
                self.rear=self.front = value

    def dequeue(self,pref=None):
            curr_node=self.front
            curr_next=curr_node.next
            deq_value=None
            # move the front to the next value and remove the current one , but first if we have one value then it will be none
            if curr_node == None:
                raise Exception("Sorry the Shelter is empty !!")
            elif pref !=self.front.kind and pref!=self.front.kind:
                return "null"
            elif self.front.kind==pref:
                deq_value=self.front
                # new front will be the next node
                self.front =self.front.next
                # if new front is none again rear should be None too

            else:
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



