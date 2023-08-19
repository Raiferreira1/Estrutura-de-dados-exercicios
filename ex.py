# def hanoi(nd,origem = 1,destino = 3):
#     if nd:
#         hanoi(nd-1,origem,6-origem-destino)
#         print(f'mova o disco {nd} da torre {origem} para a torre {destino}')
#         hanoi(nd-1,6-origem-destino,destino)


# hanoi(3)

# '''
# def hanoi(nd,origem = 1,destino = 3):
#     if nd: 3                                       nd =3, origem = 1, destino 3
#         hanoi(nd-1,origem ,6-origem-destino)
#         print(f'mova o disco {nd} da torre {origem} para a torre {destino}')
#         hanoi(nd-1,6-origem-destino,destino)


#                 if nd:                  nd  = 2    origem = 1  destino 2
#                 hanoi(nd-1,origem,6-origem-destino)
#                 print(f'mova o disco {nd} da torre {origem} para a torre {destino}')
#                 hanoi(nd-1,6-origem-destino,destino)


#                     if nd:
#                     hanoi(nd-1,origem,6-origem-destino)   nd = 2 origem = 1 destino 3

#                     print(f'mova o disco {nd} da torre {origem} para a torre {destino}')
#                     hanoi(nd-1,6-origem-destino,destino)


# def maior_numero(num):
#     if num < 10 :
#         return num

#     else:
#         lsd = num % 10
#         m = num //10

#         maior = maior_numero(m)

#         if lsd > maior:
#             return lsd

#         else: return maior

# print(maior_numero(82))


# def biggest_digit(num):
#     if num < 10 :
#         return num

#     else:
#         lsd = num % 10
#         new_num = num //10
#         bigger  = biggest_digit(new_num)

#         if lsd > bigger:
#             return lsd

#         else: return bigger

"""
def biggest_digit(num):
    if num < 10 :
        return num
    else:
        if num % 10>biggest_digit(num //10) :
            return num % 10
        else: 
            return biggest_digit(num //10)
        
print(biggest_digit(12))


"""
# func(372)  # 1
#     if 2 >func(37)   return 2             #2
#         if 7 >func(3)   return 7  #3
#             return 3
#     else
#          return func(37)


"""

# def smallest_digit(num):
#     if num < 10 :
#         return num
#     else:
#         if num % 10 < smallest_digit(num //10) :
#             return num % 10
#         else: 
#             return smallest_digit(num //10)
        
# print(smallest_digit(892))

# print(1534%10)
# print(1534//10)



# def amount_of_digits(num):
#     if num < 10 :
#         return 1
#     else:  
#           return 1 + amount_of_digits(num //10)
           
# print(amount_of_digits(892))

# def sum_digits(num):
#      if num < 10 :
#         return num
#      else:
#           return num % 10 + sum_digits(num // 10)
     
# print(sum_digits(12333)) 
     
        
          
          
   
# def rest_pair_numbers(num):
#      if num < 10 and  num % 2 == 0:
#         return 0
    
#      else:
#          return rest_pair_numbers()
     
  
     



def rest_pair_numbers(num):
    if num < 10:
       return 0 if num % 2 == 0 else num
    else:        
        if num % 2 == 0:
            return rest_pair_numbers(num // 10) * 10
        
        else:  
            return rest_pair_numbers(num // 10) * 10 + num % 10
        
 
print(rest_pair_numbers(12))


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
                        
 

# def rest_odd_numbers(num):
#     if num < 10:
#        return 0 if num % 2 != 0 else num
#     else:        
#         if num % 2 != 0:
#             return rest_odd_numbers(num // 10) * 10
        
#         else:  
#             return rest_odd_numbers(num // 10) * 10 + num % 10
        
 
# print(rest_odd_numbers(12344456))




""" """
# def remove_pair_numbers(num):

#     if num < 10:
#        return 0 if num % 2 == 0 else num
#     else:        
#         if num % 2 == 0:
#             return remove_pair_numbers(num // 10) 
        
#         else:  
#             return remove_pair_numbers(num // 10) * 10 + num % 10
        
# flag = remove_pair_numbers(1234)

# if flag == 0:
#     print('todos sao pares')

# else:
#     print(flag)


# """
# def func(1234){
#     return func(123)
#         def func (123)
#             return (func(12) * 10 + 3 )
#                  def func (12)
#                    return(1)
# }
# '''


# def remove_odd_numbers(num):

#     if num < 10:
#        return 0 if num % 2 != 0 else num
#     else:
#         if num % 2 != 0:
#             return remove_odd_numbers(num // 10)

#         else:
#             return remove_odd_numbers(num // 10) * 10 + num % 10


# # print(remove_odd_numbers(81234))

# def digit_backwards(num,backwards=0):
#      if num < 10:
#        return  backwards * 10 + num
#      else:
#          backwards = backwards * 10 + num%10

#          return digit_backwards(num//10,backwards)
# print(digit_backwards(444123))


"""
fun(123,0){
    backwards = 0 * 10 +3 = 3
    func(12,3){
         backwards = 3 * 10 + 2 =  32
            func(1,32){
                 backwards = 32 * 10 + 1 =  321
            }
    }

}
"""
