#idea: create a list of link groups of memory "cells" together using references
    #Each record contains data and a reference to the next cell.

#Node
class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def __str__(self):
        return str(self.val)
