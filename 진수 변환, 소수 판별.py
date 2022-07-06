def changeBase(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime_number(x):
    if x == 1:
         return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


"AS".isalpha()

