def organization_by_k(vetor: list[int], k: int, index=0, counter=0):

    # if vetor[index] == k:
    #       vetor.insert(0, vetor.pop(index))

    if counter == len(vetor):
        return vetor

    else:
        if vetor[index] <= k:
            return organization_by_k(vetor, k, index + 1, counter + 1)

        else:
            vetor.append(vetor.pop(index))
            return organization_by_k(vetor, k, index, counter + 1)


print(organization_by_k([1, 0, 2, 9, 3, 8, 4, 7, 5, 6, 11, 22, 33, 44, 37], 5))























# def func(vetor, k, caut=0, index=0):
#     if index == len(vetor) - 1:
#         return vetor

#     else:
#         if vetor[caut] <= k:
#             return func(vetor, k, caut + 1, index + 1)
#         else:
#             vetor.append(vetor.pop(caut))
#             return func(vetor, k, caut + 1, index + 1)


# print(func([1, 3, 4, 5, 4, 5, 6, 78, 3, 6, 7, 8], 2))
