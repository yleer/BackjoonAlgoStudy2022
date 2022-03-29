import sys

n = int(input())
data = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    data.append(tmp)


dp = [[data[0][0]]]

# print(data)
# print(dp)


for i in range(1, n):
    currentArray = data[i]
    prevArray = dp[-1]
    tmp = []

    for i in range(len(currentArray)):
        if i == 0:
            tmp.append(currentArray[i] + prevArray[0])
        elif i == len(currentArray) - 1:
            tmp.append(prevArray[-1] + currentArray[i])
        else:
            tmp.append(max(prevArray[i], prevArray[i-1]) + currentArray[i])
    dp.append(tmp)
print(max(dp[-1]))
