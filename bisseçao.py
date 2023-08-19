def f(x):
    return x * 3 - 2 * x + 10


def bissecao(f, a, b, e=0.01):
    cont = 0
    while abs(a - b) > e:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        print(cont)
        cont += 1
    return (a + b) / 2


print(bissecao(f, -3, 0))
