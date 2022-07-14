import sys

n, m = map(int, sys.stdin.readline().split())


if m >= 45:
    print(n, m - 45)
else:
    toAdd = 60 - 45
    m = m + toAdd

    if n == 0:
        print(23, m)
    else:
        print(n-1, m)