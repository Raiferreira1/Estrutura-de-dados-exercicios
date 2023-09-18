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

    
  def insertInSortedOrder(self, data):
        new_node = Node(data)

        if self.length == 0 or self.head.data > data:
            self.insertAtBeginning(data)
            return

        current = self.head
        previous = None

        while current is not None and current.data <= data:
            previous = current
            current = current.next

     
        previous.next = new_node
        new_node.next = current
        self.length += 1



  def getNthElement(self, n):
        if n < 0:
            raise ValueError("O valor de n deve ser não negativo")

        fast = slow = self.head
        count = 0

        while count < n and fast:
            fast = fast.next
            count += 1

        if count < n or fast is None:
            raise ValueError("O valor de n excede o tamanho da lista")

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        return slow.data
    
  def printReverseLL(self,head):
     if head is None:
        return
     self.printReverseLL(head.next)
     print(head.data)


  def deleteAtValue(self, value):
    current = self.head
    previous = None

    while current:  

        if current.data == value:
            if previous is None: 
                self.head = current.next
            else:
                previous.next = current.next

            self.length -= 1
        else:
            previous = current

        current = current.next
    
  def moveElementsToFront(self,k):
      if self.length <= 1:
        return
      current = self.head.next
      previous = self.head

      while current:
          if current.data == k:
              previous.next = current.next
              current.next = self.head
              self.head = current
              current = previous.next
          else:
                previous = current
                current = current.next
    



  def reverse_linked_list(self, head):
        prev = None
        current = head   
        while current:                       
            next_node = current.next                  
            current.next = prev                             
            prev = current                                     
            current = next_node                               

        return prev                                           





  def is_palindrome(self):
        if self.length <= 1:
            return True  

        middle = self.length // 2       

        current = self.head
        
        for _ in range(middle):
            current = current.next        

        if self.length % 2 == 0:
            second_half = self.reverse_linked_list(current)
        else:
             second_half = self.reverse_linked_list(current.next)

        first_half = self.head
        while second_half:
            if first_half.data != second_half.data:
                return False  
            second_half = second_half.next
            first_half =  first_half.next
        

        return True 