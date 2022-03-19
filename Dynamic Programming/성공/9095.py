n = int(input())

num = []
for i in range(n):
    tmp = int(input())
    num.append(tmp)

maxNum = max(num)

maxNum

dp = []
for i in range(maxNum + 1):
    if i == 0:
        dp.append(0)
    elif i == 1:
        dp.append(1)
    elif i == 2:
        dp.append(2)
    elif i == 3:
        dp.append(4)
    else:
        tmp = dp[i - 1] + dp[i - 2] + dp[i - 3]
        dp.append(tmp)

for i in range(n):
    print(dp[num[i]])





