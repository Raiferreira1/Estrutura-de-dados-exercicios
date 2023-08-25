class Node:
    def __init__ (self, data=None, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    #Add getters and setters
    def __str__(self):
        return "Node[Data=%s]" % self.data
    