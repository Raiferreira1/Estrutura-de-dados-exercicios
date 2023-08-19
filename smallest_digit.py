def smallest_digit(num):
    if num < 10:
        return num
    else:
        if num % 10 < smallest_digit(num // 10):
            return num % 10
        else:
            return smallest_digit(num // 10)
