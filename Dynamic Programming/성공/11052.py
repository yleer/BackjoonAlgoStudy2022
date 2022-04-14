import sys
input = sys.stdin.readline
n = int(input())



prices  = list(map(int, sys.stdin.readline().strip().split()))
prices.insert(0,0)
dp = [0] * (n+1)

dp[1] = prices[1]
dp[2] = max(prices[1]*2, prices[2])
for i in range(3,n+1):
    dp[i] = prices[i]
    for j in range(1, i):
        dp[i] = max(dp[i],dp[j] + prices[i-j])



print(max(dp))

