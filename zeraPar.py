def zeraPar(n):
    if n < 10 and n % 2 == 0:
        return 0
    elif n < 10 and n % 2 == 1:
        return n
    else:
        if n % 2 == 0:
            return zeraPar(n // 10) * 10
        else:
            return zeraPar(n // 10) * 10 + n % 10


print(zeraPar(8498613))
