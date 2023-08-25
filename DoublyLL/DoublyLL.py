from Node import Node

class DoublyLL:
    
    def __init__(self):
        self.length = 0
        self.head=None
        self.tail=None

    def insertAtGivenPosition(self, pos, data):
        if self.head==None or pos ==0:
            self.insertAtBeginning(data)
        elif pos == self.length:
            self.insertAtEnd(data)
        elif pos < self.length:
            curr = self.head
            count = 0 
            while curr != None and count < pos:
                curr = curr.next
                count +=1
            newNode = Node(data)
            newNode.next = curr.next
            newNode.prev = curr
            curr.next = newNode
            length += 1
    
    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if(self.head==None):
            self.head = self.tail = newNode
        else:
            newNode.prev=None
            newNode.next=self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def insertAtEnd(self,data):
        if (self.head==None):
            self.head = self.tail= Node(data)
        else:
            current = self.head
            while(current.next!=None):
                current=current.next
            
            newNode = Node(data)
            current.next = newNode
            newNode.prev = current
            newNode.next = None
            self.tail=newNode
        self.length +=1
    

        
   
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=",")
            current = current.next



        
    def deleteFromBeginning(self):
        if self.length != 0:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None

            else:
                self.tail = None
            self.length -= 1    


        
    def deleteFromEnd(self):
        if self.length != 0:
          self.tail = self.tail.prev

        if self.tail is not None:
            self.tail.next = None

        else:
            self.head = None
            self.length -= 1  
    



    
def removeByBinarySearch(l, index):
    if index < 0 or index >= l.length:
        return None 
        
    if index == 0:
        l.deleteFromBeginning()

    elif index == -1:
       l.deleteFromEnd()
    
    aux = l.length // 2
    
    if index <= aux:
        cont = 0
        current_node = l.head
        while current_node and cont < index:
            current_node = current_node.next
            cont += 1

        current_node.prev.next = current_node.next
        if current_node.next:
            current_node.next.prev = current_node.prev
    else:
        cont = l.length - 1
        current_node = l.tail
        while current_node and cont > index:
            current_node = current_node.prev
            cont -= 1

        current_node.prev.next = current_node.next
        if current_node.next:
            current_node.next.prev = current_node.prev