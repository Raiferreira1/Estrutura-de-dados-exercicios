def zero_even_numbers(num):
    if num < 10:
        return 0 if num % 2 == 0 else num
    else:
        if num % 2 == 0:
            return zero_even_numbers(num // 10) * 10

        else:
            return zero_even_numbers(num // 10) * 10 + num % 10


print(zero_even_numbers(1234))


"""
# def rest_pair_numbers(1234){
#     return rest_pair_numbers(123) * 10
#         def rest_pair_numbers(123) {
#             return rest_pair_numbers(12) * 10 + 3
#                 def rest_pair_numbers(12){
#                     return rest_pair_numbers(1) * 10
#                         def rest_pair_numbers(1){
#                             return 1
#                        }
#                 }
#         }
# }


"""
