from Node import Node


class LinkedList(object):

  def __init__(self):
    self.length = 0
    self.head = None


  def insertAtBeginning(self, data):
    new_node = Node(data)  
    if self.length == 0:
        self.head = new_node
    else:
        new_node.next = self.head  
        self.head = new_node  
    self.length += 1  


  def insertAtGivenPosition(self, pos, data):
    if pos > self.length or pos < 0:
        return None

    new_node = Node(data)  

    if pos == 0:
        new_node.next = self.head  
        self.head = new_node  
    else:
        current = self.head
        count = 0
        while count < pos - 1:
            current = current.next
            count += 1
        new_node.next = current.next  
        current.next = new_node  

    self.length += 1  


  def insertAtEnd(self, data):
    new_node = Node(data)  
    
    if self.length == 0:
        self.head = new_node  
    else:
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node  
    
    self.length += 1  


  def deleteAtPosition(self, pos):
    if pos >= self.length or pos < 0:
        return None

    if pos == 0:
        self.head = self.head.next
        self.length -= 1
        return

    current = self.head
    previous = None
    count = 0

    while count < pos:
        previous = current
        current = current.next
        count += 1

    previous.next = current.next
    self.length -= 1


  

  def deleteFromBeginning(self):
      if self.length > 0:
          self.head = self.head.next
          self.length -= 1

  def deleteFromEnd(self):
      if self.length > 0:
          if self.length == 1:
              self.head = None
          else:
              current = self.head
              previous = None
              while current.next is not None:
                  previous = current
                  current = current.next
              previous.next = None
          self.length -= 1

  def printList(self):
    current = self.head
    pos = 0
    while current and pos < self.length:
        print("Node %d has value %s" % (pos, current.data))
        current = current.next
        pos += 1

  def getNodeAtPosition(self, index):
    if 0 <= index < self.length:
        current = self.head
        for i in range(index):
            current = current.next
        return current
    return None

