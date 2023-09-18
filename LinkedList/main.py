from LinkedList import LinkedList




def removerPares(lista):
    if lista.length == 0:
        return
    atual = anterior = lista.head
    while atual:
        if atual.data % 2 == 0:
            if atual == lista.head:
                lista.head = atual.next
                atual = anterior = lista.head
            anterior.next = atual.next 
        else:
            anterior = atual
        atual = atual.next
    return lista

list = LinkedList()
list.insertAtEnd(2)
list.insertAtEnd(1)
# list.insertAtEnd(3)
# list.insertAtEnd(3)
# list.insertAtEnd(2)
# list.insertAtEnd(1)

# list.moveElementsToFront(3)
print("Original list:")
print()

list.printList()


# print(list.reverse_linked_list())
removerPares(list)
print()


print("New list:")
list.printList()


# print("New list:")
# list.printReverseLL(list.head)







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

  



