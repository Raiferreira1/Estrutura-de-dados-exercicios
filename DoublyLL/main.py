from DoublyLL import DoublyLL



doubly_list = DoublyLL()

doubly_list.insertAtBeginning(9)
doubly_list.insertAtBeginning(5)
doubly_list.insertAtEnd(2)
doubly_list.insertAtEnd(7)

print("Original list:")
doubly_list.printList()

doubly_list.deleteFromBeginning()
doubly_list.deleteFromEnd()
doubly_list.insertAtEnd(9)
doubly_list.insertAtBeginning(7)


print("New list:")
doubly_list.printList()

# doubly_list.deleteAtPosition(-1)
doubly_list.deleteAtPosition(1)


print("New list: ")
doubly_list.printList()

print(doubly_list.length)