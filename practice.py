import sys


m = int(input())
arr = []
for i in range(m):
    n, w = list(map(int, sys.stdin.readline().strip().split()))
    arr.append([n, w])


arr.sort()

answer = 0
best = arr[0]
for i in range(1,len(arr)):
    curr = arr[i]

    if best[0] < curr[0] and best[1] < curr[1]:
        answer += 1
    elif best[0] > curr[0] and best[1] < curr[1]:
        best = [best[0], best[1]]
    elif best[0] < curr[0] and best[1] > curr[1]:
        best = [curr[0], curr[1]]
    else:
        continue

print(answer)