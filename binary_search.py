def binary_search(n, target, low=0, high=None):
    if high is None:
    high = len(vetor)-1


    if low > high:
        return False
    

    if n[(low + high) // 2] == target:
        return True


    else:
        if target > n[(low + high) // 2]:
            return binary_search(n, target, ((low + high) // 2) + 1, high)
        else:
            return binary_search(n, target, low, ((low + high) // 2) - 1)


print(binary_search([1, 4, 5, 7, 8, 10, 12, 15, 20, 45, 67] ,52, 0, 11))
# print(binary_search([1, 2,3,5], 4, 0, 3))

# print(binary_search(range(10), 3, 0, 9))


# def binary_search(n, target, low=0, high=0):

#     if low > high:
#         return False
    
#     if n[(low + high) // 2] == target:
#         return True

#     else:
#         if target > n[(low + high) // 2]:
#             return binary_search(n, target, ((low + high) // 2) + 1, high)
#         else:
#             return binary_search(n, target, low, ((low + high) // 2) - 1)
        

# print(binary_search([1, 2,3,5], 1000, 0, 3))
