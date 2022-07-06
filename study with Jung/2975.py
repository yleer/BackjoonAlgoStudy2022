import sys


while True:
    a = list(map(str, sys.stdin.readline().split()))
    if a[0] == "0" and a[1] == "W" and a[2] == "0":
        break

    start = int(a[0])
    transaction = int(a[2])

    if a[1] == "W":
        if start - transaction < -200:
            print("Not allowed")
        else:
            print(start - transaction)
    else:
        if start + transaction < -200:
            print("Not allowed")
        else:
            print(start + transaction)



