def backwardDigits(num, backwards=0):
    if num == 0:
        return backwards
    else:
        # backwards = backwards * 10 + num % 10

        return backwardDigits(num // 10, backwards * 10 + num % 10)


# print(backwardDigits(444123))


def inverte(n, inversao=0):
    if n < 10:
        return inversao * 10 + n
    else:
        return inverte(n // 10, n % 10 + 10 * inversao)


print( backwardDigits(123))

print(inverte(123))
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
