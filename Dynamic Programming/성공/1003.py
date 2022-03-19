n = int(input())

num = []
for i in range(n):
    tmp = int(input())
    num.append(tmp)

a = max(num)
dp = [[1,0], [0,1]]


for i in range(a + 1):
    if i == 0 or i == 1:
        pass
    else:
        first_zero = dp[i-1][0]
        first_one = dp[i-1][1]
        second_zero = dp[i-2][0]
        second_one = dp[i-2][1]

        new = [first_zero + second_zero, first_one + second_one]
        dp.append(new)


for i in range(n):
    print(dp[num[i]][0], dp[num[i]][1])
