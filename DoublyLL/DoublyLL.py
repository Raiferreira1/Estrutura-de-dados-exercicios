from Node import Node

class DoublyLL:
    
    def __init__(self):
        self.length = 0
        self.head=None
        self.tail=None

   
    def insertAtGivenPosition(self, pos, data):
        if self.head is None or pos == 0:
            self.insertAtBeginning(data)

        elif pos == self.length:
            self.insertAtEnd(data)

        elif 0 < pos < self.length:
            current = self.head
            count = 0

            while current and count < pos:
                current = current.next
                count += 1

            new_node = Node(data)
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

            self.length += 1


    def insertAtBeginning(self, data):
        new_node = Node(data, self.head, None)

        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node

        self.head = new_node
        self.length += 1


    def insertAtEnd(self, data):
        new_node = Node(data, None, self.tail)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1

        
    def printList(self):
        current = self.head
        while current:
            print(current.data, end="")
            if current.next:
                print(", ", end="")
            current = current.next
        print()

  
    def deleteFromBeginning(self):
        if self.length > 0:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            self.length -= 1    


        
    def deleteFromEnd(self):
        if self.length > 0:
          self.tail = self.tail.prev

        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.length -= 1  
    

        
    def deleteAtPosition(self, index):
        if index < 0 or index >= self.length:
            return None 
        
        if index == 0:
            self.deleteFromBeginning()
        elif index == self.length - 1:
            self.deleteFromEnd()
        else:
            is_closer_to_beginning = index < self.length // 2

            current_node = self.head if is_closer_to_beginning else self.tail
            count = 0 if is_closer_to_beginning else self.length - 1

            while count != index:
                if is_closer_to_beginning:
                    current_node = current_node.next
                    count += 1
                else:
                    current_node = current_node.prev
                    count -= 1
                
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            
            self.length -= 1
    


    def deleteAtValue(self, value):
        current = self.head
    
        while current:
            if current.data == value:
                if current.prev is None:
                    self.deleteFromBeginning()
                elif current.next is None:
                    self.deleteFromEnd()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.length -= 1
           
            
            current = current.next
