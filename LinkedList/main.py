from LinkedList import LinkedList


list = LinkedList()
list.insertAtEnd(0)
list.insertAtEnd(3)
list.insertAtEnd(2)
list.insertAtEnd(3)
list.insertAtEnd(4)

list.moveElementsToFront(3)
print("Original list:")
list.printList()

list.insertInSortedOrder(2)

print("New list:")
list.printReverseLL(list.head)







# def kkkk(l, n):
        


#         size = 0
#         now = l.head
#         while now:
#             size += 1
#             now = now.next

#         if n < 0 or n > size:
#             return None
        
#         position = l.length - n -1

#         current = l.head

#         while position > 0:
#             current = current.next
#             position-=1
#         return current.data

  



