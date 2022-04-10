n = int(input())

dp = []
for i in range(n):
    a = [0] * 10
    if i == 0:
        a = [0,1,1,1,1,1,1,1,1,1]

    dp.append(a)

# print(dp)


for i in range(n):
    for j in range(0,10):
        if i == 0:
            pass
        else:
            if j == 0:
                # print(i,j)
                dp[i][j] = dp[i-1][j+1]
            else:
                # print(i,j)
                if j != 9:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
                else:
                    dp[i][j] = dp[i-1][j-1]





# print(dp)
print(sum(dp[-1]) % 1000000000)
