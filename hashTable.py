# Author = "Piyush Makhija"

# Hash Table class definition
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in the table."""
        index = self.calculate_hash_value(string)
        if index != -1:
            if self.table[index] != None:
                self.table[index].append(string)
            else:
                self.table[index] = [string]
        
    def lookup(self, string):
        """Return the hash value if the string is already in the table.
        Return -1 otherwise."""
        index = self.calculate_hash_value(string)
        if index != -1 and self.table[index] != None:
            if string in self.table[index]:
                return index
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a hash value from a string."""
        index = ord(string[0])*100 + ord(string[1])
        return index
