import sys

n = int(input())
li = list(map(int, sys.stdin.readline().split()))
price = int(input())
li.sort()
if sum(li) <= price:
    print(li[-1])

else:
    affordable = int(price / n)
    for i in range(len(li)):
        if affordable >= li[i]:
            price = price - li[i]
            affordable = int(price / (n-i-1))
            li[i] = 0

    num = 0
    for i in range(len(li)):
        if li[i] > 0 :
            num += 1

    print(int(price/ num))

