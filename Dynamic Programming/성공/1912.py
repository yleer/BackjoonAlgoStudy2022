import sys

n = int(input())

array = list(map(int, sys.stdin.readline().strip().split()))

dp = [array[0]]

for i in range(1,n):
    tmp = max(array[i], dp[i - 1] + array[i])
    dp.append(tmp)

print(max(dp))
