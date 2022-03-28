n = int(input())


array = [0]
for i in range(n):
    tmp = int(input())
    array.append(tmp)

if n == 1:
    print(array[1])
elif n == 2:
    print(array[1] + array[2])
else :




    dp = [0, array[1], array[1] + array[2]]

    # print(array)

    for i in range(3,n+1):
        t = max(dp[i - 3] + array[i-1] + array[i], dp[i -2]+array[i])
        t2 = max(t, dp[i-1])
        dp.append(t2)

    # print(dp)
    print(max(dp))


