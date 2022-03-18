import  sys

n, w = map(int, sys.stdin.readline().strip().split())
array = []

for i in range(0,n ):
    tmp1, tmp2 = map(int, sys.stdin.readline().strip().split())
    array.append([tmp1,tmp2])


dp = []

for i in range(0, n + 1):
    tmpDp = []
    for j in range(0, w + 1):
        if i == 0 or j == 0:
            tmpDp.append(0)
        else:
            syncI = i - 1
            if array[syncI][0] > j:
                tmpDp.append(dp[syncI][j])
            else:
                tmpDp.append(max(dp[syncI][j], array[syncI][1] + dp[syncI][j - array[syncI][0]]))

    dp.append(tmpDp)


print(dp[n][w])

