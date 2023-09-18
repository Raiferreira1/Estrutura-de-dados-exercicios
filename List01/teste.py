def removerPares(lista):
    if lista.length == 0:
        return
    atual = anterior = lista.head
    while atual:
        if atual.data % 2 == 0:
            if atual == lista.head:
                lista.head = atual.next
                atual = anterior = lista.head
            anterior.next = atual.next #[1, 2, 3, 4, 6, 8]
        else:
            anterior = atual
        atual = atual.next
    return lista

def somarImpares(lista):
    if lista.length == 0:
        return
    soma = 0
    atual = lista.head
    while atual:
        if atual.data % 2:
            soma += atual.data
        atual = atual.next
    return soma

def dividirListaEncadeada(lista):
    if lista.length <= 1:
        return
    
    lc1 = LinkedList()
    lc2 = LinkedList()

    lc1.length = lista.length // 2
    atual = lc1.head = lista.head

    for i in range(lc1.length - 1):
        atual = atual.next

    lc2.head = atual.next
    lc2.length = lista.length - lc1.length
    atual.next = lc1.head
    
    atual = lc2.head
    for i in range(lc2.length - 1):
        atual = atual.next
    atual.next = lc2.head

    lc1.printElements()
    lc2.printElements()

def entrelacarListasEncadeadas(lista1, lista2):
    lista3 = LinkedList()
    atualLista1 = lista1.head
    atualLista2 = lista2.head
    while atualLista1 and atualLista2:
        lista3.insertAtEnd(atualLista1.data)
        lista3.insertAtEnd(atualLista2.data)
        atualLista1 = atualLista1.next
        atualLista2 = atualLista2.next
    if lista1.length > lista2.length:
        while atualLista1:
            lista3.insertAtEnd(atualLista1.data)
            atualLista1 = atualLista1.next
    elif lista1.length < lista2.length:
        while atualLista2:
            lista3.insertAtEnd(atualLista2.data)
            atualLista2 = atualLista2.next
    return lista3