from node import Node

class Linkedlist:
    def __init__(self):
        self.first = None

class LinkedList:

    def find(self, key):
        current = self.first
        while current and current.val != key:
            current = current.next

        return current

    def insert_first(self, val):
        new_node = Node(val)
        
    def delete(selfself, key):
        current = self.first
        previous = self.first

    while current.val != key:
        if current == self.first:
            self.first = self.first.next

        if current.next == None:
            return None

        else:
            previous = current

            return current

    def display(self):
        print(
