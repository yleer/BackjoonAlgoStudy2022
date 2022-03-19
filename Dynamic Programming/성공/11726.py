n = int(input())

dp = [0, 1,2,3]

for i in range(n + 1):
    if i == 0 or i == 1 or i == 2 or i == 3:
        pass
    else:
        prev = dp[i - 1]
        prev_prev = dp[i - 2]

        tmp = prev + prev_prev
        dp.append(tmp)


print(dp[n] % 10007)
