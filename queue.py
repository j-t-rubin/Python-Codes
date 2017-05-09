# Author = "Piyush Makhija"

# Queue Class Definition
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        """ Enque new element to the end of Queue """
        self.storage.append(new_element)

    def peek(self):
        """ Get/Peek first elemnt to Queue """
        return self.storage[0]

    def dequeue(self):
        """ Dequeue first elemnt from the Queue """
        dequed = self.storage[0]
        self.storage = self.storage[1:]
        return dequed
