import heapq
import sys

input = sys.stdin.readline
n = int(input())

ar = []
for i in range(n):
    tmp = int(input())
    heapq.heappush(ar, tmp)


if len(ar) > 1 :
    sum = 0
    while len(ar) != 0:
        frist = heapq.heappop(ar)
        second = heapq.heappop(ar)
        sum2 = frist + second
        sum += sum2
        if len(ar) == 0:
            break
        heapq.heappush(ar, sum2)

    print(sum)
else :
    print("0")




