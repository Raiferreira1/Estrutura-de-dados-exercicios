
# def potenciaPorAdicao(c, n):
#     cont = resposta = 0
#     for i in range(c ** (n - 1)):
#         resposta += c
#         cont += 1
#         print(resposta)

#     print(f'c^n = {c ** n} // {resposta}')
#     print(f'Iterações: {cont}')

# potenciaPorAdicao(3,2)



def exemple1(s):
    n = len(s)
    t= 0
    for j in range(n):
        # print(j)
        for k in range( j + 1):
            print(k , end= "\n")
            t+= s[k]
    return 

l = [1,2]

print(exemple1(l))





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