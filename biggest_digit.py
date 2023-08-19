# def biggest_digit(num):
#     if num < 10 :
#         return num

#     else:
#         lsd = num % 10
#         new_num = num //10
#         bigger  = biggest_digit(new_num)

#         if lsd > bigger:
#             return lsd

#         else:
#             return bigger


def biggest_digit(num):
    if num < 10:
        return num
    else:
        if num % 10 > biggest_digit(num // 10):
            return num % 10
        else:
            return biggest_digit(num // 10)


print(biggest_digit(4351))
# print(f"{c}")

"""
    func(1234)                            #0
        if 4 >func(123)   return 4        #1
            if 3 >func(12)   return 3     #2
                if 2 >func(1)   return 2  #3
                     return num 
"""

"""
 func(4321)                            #0
        if 1 >func(432)   return 1      #1
            if 2 >func(43)   return 2    #2
                if 3 >func(4)   return 3  #3
                     return num
                else
                   return func(4) #4  
            else 
               return func(43)  
                    if 3 > func(4) return 3  
                       return 4
        else
            return func(432)
                if  2 > func(43) return 2
                   if 3 > func(4) return 3
                        returrn 4
                   else
                       return func(4)
                else 
                    return func(43)
                      if 3 > func(4) return 3  
                        return 4
                     else 
                    
                




"""


#  func(4521)                            #0
#         if 1 >func(452)   return 1      #1
#             if 2 >func(45)   return 2    #2
#                 if 5 >func(4)   return 5  #3
#                      return num
#


#   func(4351)                            #0
#         if 1 >func(435)   return 1      #1
#             if 5 >func(43)   return 5    #2
#                 if 3 >func(4)   return 3  #3
#                      return num
#
