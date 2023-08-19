def zero_odd_numbers(num):
    if num < 10:
        return 0 if num % 2 == 1 else num
    else:
        if num % 2 == 1:
            return zero_odd_numbers(num // 10) * 10

        else:
            return zero_odd_numbers(num // 10) * 10 + num % 10


print(zero_odd_numbers(1234))


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
