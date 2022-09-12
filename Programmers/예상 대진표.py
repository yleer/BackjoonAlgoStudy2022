n, a, b = 8,4,7


if a > b:
    a, b = b, a


## a < b
count = 1

while True:
    if b - 1 == a and b % 2 == 0:
        break

    if a % 2 == 1:
        a = (a + 1) / 2
    else:
        a = a / 2

    if b % 2 == 1:
        b = (b+1) / 2
    else:
        b = b / 2
    count += 1

print(count)