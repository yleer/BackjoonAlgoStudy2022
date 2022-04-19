import math

n = 524287
k = 2
# 524287,2


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



a = changeBase(n,k)
print(a)

zeros = []
answer = 0
t = ""
for i in range(len(a)):
    if a[i] == "0":
        if len(zeros) == 0:
            if is_prime_number(int(a[:i])):
                answer += 1
                # print("zz")
            t = ""
            zeros.append(i)
        else:
            print(t,i)
            if len(t) > 0:
                if is_prime_number(int(t)):
                    answer += 1
                    # print("bb", t)
            t = ""
            zeros.append(i)
    else:
        t = t + a[i]

print("b")
if len(t) > 0:
    if is_prime_number(int(t)):
        answer += 1
# print("b")
print(answer)