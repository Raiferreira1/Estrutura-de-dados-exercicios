from Node import Node


class CircularLL:
    def __init__(self):
        self.length = 0
        self.head = None
    
    def insertAtBeginning(self, data):
        new_node = Node(data, self.head)
        if self.head is None:
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node
        self.length += 1
        
    def insertAtEnd(self, data):
        new_node = Node(data, self.head)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def insertAtGivenPosition(self, pos, data):
        if pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.length:
            self.insertAtEnd(data)
        elif 0 < pos < self.length:
            new_node = Node(data)
            current = self.head
            count = 0
            while count < pos - 1:
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node
            self.length += 1
    
    def deleteFromBeginning(self):
        if self.length > 0:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            self.length -= 1

    def deleteFromEnd(self):
        if self.length > 0:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head
            self.length -= 1

    def deleteAtPosition(self, pos):
        if pos < 0 or pos >= self.length:
            return None
        
        if pos == 0:
            self.deleteFromBeginning()
        elif pos == self.length - 1:
            self.deleteFromEnd()
        else:
            current = self.head
            count = 0
            while count < pos - 1:
                current = current.next
                count += 1
            current.next = current.next.next
            self.length -= 1
    
    def printList(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end="")
            current = current.next
            if current == self.head:
                break
            print(", ", end="")
        print("")
