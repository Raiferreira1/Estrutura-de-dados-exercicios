from LinkedList import LinkedList

def removeNodesWithValue(l, v):
    current = l.head
    previous = None

    while current is not None:  

        if current.data == v:
            if previous is None: 
                l.head = current.next
            else:
                previous.next = current.next

            l.length -= 1
        else:
            previous = current

        current = current.next




  

# def removeNodesWithValue(l, x):

#     while l.head is not None and l.head.data == x:
#         l.deleteFromBeginning()
#     current = l.head
 

#     while current is not None:
#         if current.data == x:
#             if current.next is None:
#                 l.deleteFromEnd()
#             else:
#                 position =l.getPosition(current)
#                 l.deleteAtPosition(position)  
#         current = current.next


list = LinkedList()
list.insertAtEnd(5)
list.insertAtEnd(10)
list.insertAtEnd(15)
list.insertAtEnd(10)
list.insertAtEnd(20)

print("Original list:")
list.print()

v = 10
removeNodesWithValue(list,v)

print("New list:")
list.print()
