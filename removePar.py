def removePar(n):
    if n < 10:
        if n % 2 == 0:
            return 0
        else:
            return n
    else:
        if n % 2 == 0:
            return removePar(n // 10)
        else:
            return removePar(n // 10) * 10 + n % 10


print(removePar(77885569))
