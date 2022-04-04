import sys

n = int(input())
array = []
for i in range(n):
    t = list(map(int, sys.stdin.readline().strip().split()))
    array.append(t)

array.sort(key = lambda x:(x[1], x[0]))

workingTime = []
ableCount = 0
for i in range(n):

    start, end = array[i]

    if len(workingTime) == 0:
        ableCount = ableCount + 1
        workingTime.append(end)
    else:
        if workingTime[-1] <= start:
            ableCount = ableCount + 1
            workingTime.append(end)


# print(workingTime)
print(ableCount)
