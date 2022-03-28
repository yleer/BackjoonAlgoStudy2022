n = int(input())

stairs = [0]

for i in range(n):
    t = int(input())
    stairs.append(t)

if n >= 3:
    dp = [stairs[0], stairs[1], stairs[1] + stairs[2]]

    for i in range(3,n+1):
        maxNum = stairs[i] + max(dp[i-2], dp[i-3] + stairs[i-1])
        dp.append(maxNum)

    print(dp[-1])
else:
    if n == 2:
        print(stairs[1] + stairs[2])
    else:
        print(stairs[1])
