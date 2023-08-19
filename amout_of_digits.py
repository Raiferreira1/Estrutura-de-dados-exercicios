def amount_of_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + amount_of_digits(num // 10)


print(amount_of_digits(1234))

"""
    func(1234){ #0
        return 1 + func(123) #1
           return 1 + func(12) #2
            return 1 + func(1) #3
                 return 1
    }
"""
