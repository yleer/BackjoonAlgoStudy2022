import sys

n = int(input())

array = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    array.append(tmp)

dp = [[array[0][0],array[0][1],array[0][2]]]


for i in range(1, n):
    curr = array[i]
    prev = dp[i - 1]


    t = []
    for j in range(len(curr)):
        if j == 0:
            t.append(min(prev[1], prev[2]) + curr[j])
        elif j == 1:
            t.append(min(prev[0], prev[2]) + curr[j])
        elif j == 2:
            t.append(min(prev[1], prev[0]) + curr[j])

    dp.append(t)



print(min(dp[-1]))
