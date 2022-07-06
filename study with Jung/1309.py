

n = int(input())
a = [1] * (n+1)


a[1] = 3

for i in range(1, n + 1):
    if i > 1:
        a[i] = a[i-1] * 2 + a[i-2]
        a[i] = a[i] % 9901



print(a[n])


