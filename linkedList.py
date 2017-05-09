class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """ Get node from specified position
        Returns None if node is not found in list """
        current = self.head
        i=1
        while current and i<=position:
            if i == position:
                return current
            current = current.next
            i = i+1
        return None

    def insert(self, new_element, position):
        """ Insert new node at specified position """
        current = self.head
        i=1
        if position > 1:
            while current and i<position:
                if i == position-1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                i = i+1
        elif position ==1:
            new_element.next = self.head
            self.head = new_element
            
    def delete(self, value):
        """ Delete the first node with specified value """
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
