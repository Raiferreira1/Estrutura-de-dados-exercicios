from CircularLL import CircularLL



circular_list = CircularLL()

circular_list.insertAtBeginning(9)
circular_list.insertAtBeginning(5)
circular_list.insertAtEnd(2)
circular_list.insertAtEnd(7)
circular_list.insertAtGivenPosition(2,3)

print("Original list:")
circular_list.printList()

circular_list.deleteFromBeginning()
circular_list.deleteFromEnd()
circular_list.insertAtEnd(9)
circular_list.insertAtBeginning(7)


print("New list:")
circular_list.printList()

circular_list.deleteAtPosition(4)

print("New list: ")
circular_list.printList()

print(circular_list.length)


























    
#     def kkkk(self, n):
#         # Calcula o tamanho da lista
#         size = 0
#         current = self.head
#         while current:
#             size += 1
#             current = current.next
        
#         # Verifica se n é válido
#         if n <= 0 or n > size:
#             return None
        
#         # Calcula a posição do n-ésimo nó a partir do início
#         position = size - n
        
#         # Encontra o n-ésimo nó a partir do início
#         current = self.head
#         for i in range(position):
#             current = current.next
        
#         return current.data
