import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    k, w = map(int, sys.stdin.readline().strip().split())

    arr.append([w,k])

dp = []
for i in range(n+1):
    t = [0] * (n+1)
    dp.append(t)


for i in range(n):
    curr = arr[i]
    for j in range(n):

        if dp[i][j] == -1:
            continue
        if i > j:
            dp[i][j] = -1
        elif i == j:

            if curr[1] + j - 1 <= n -1:
                # print(i, j, "gg")
                dp[i][j + curr[1]] += curr[0]
                # print(i,dp[i])
                for k in range(j+1, j + 1 + curr[1] -1):
                    if dp[i][k] ==0:
                        dp[i][k] = -1

                # print(i,dp[i])
                # print()

            else:
                dp[i][j] = -1

        else:
            if dp[i][j] == -1:
                pass
            else:
                if curr[1] + j - 1 <= n - 1:
                    # print(i, curr[0], dp[i][j+curr[1]], dp[i][j])
                    dp[i][j + curr[1]] += curr[0] + dp[i][j]
                    for k in range(j + 1, j + 1 + curr[1] - 1):
                        dp[i][k] = -1

                # else:
                #     if dp[i][j] !=0 :
                #





maxNum = 0
for a in dp:
    maxNum = max(max(a), maxNum)

print(maxNum)





print(dp)
# [[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], [0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0], [0, 0, 0, -1, -1, -1, -1, -1, -1, -1, 0], [0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, -1, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0], [0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]