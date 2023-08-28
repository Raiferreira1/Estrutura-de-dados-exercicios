from LinkedList import LinkedList

def deleteAtValue(l, value):
    current = l.head
    previous = None

    while current:  

        if current.data == v:
            if previous is None: 
                l.head = current.next
            else:
                previous.next = current.next

            l.length -= 1
        else:
            previous = current

        current = current.next




  



list = LinkedList()
list.insertAtEnd(5)
list.insertAtEnd(10)
list.insertAtEnd(15)
list.insertAtEnd(10)
list.insertAtEnd(20)
list.insertAtGivenPosition(5,55)
# list.deleteAtPosition(0)

print("Original list:")
list.printList()

v = 5


print("New list:")
list.printList()
