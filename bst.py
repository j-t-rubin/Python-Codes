# Author = "Piyush Makhija"

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Search Tree class definition 
class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """ Insert new value in Binary search Tree """
        cur = self.root
        while cur.value != new_val:
            if cur < new_val:
                if cur.left == None:
                    cur.left.value = Node(new_val)
                cur = cur.left
            if cur > new_val:
                if cur.right == None:
                    cur.right = Node(new_val)
                cur = cur.right

    def search(self, find_val):
        """ Search for specified value in BST. Return True if found, else return False """
        cur = self.root
        while cur != None:
            if cur.value == find_val:
                return True
            elif cur.value < find_val:
                cur = cur.left
            elif cur.value > find_val:
                cur = cur.right
        return False
