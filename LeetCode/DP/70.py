n = 5

dp = [1,2]

for i in range(2,n ):
    cur = dp[i-1] + dp[i-2]
    dp.append(cur)


print(dp)