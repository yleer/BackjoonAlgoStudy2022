import sys
input = sys.stdin.readline
n = int(input())

dp = [1,2]
if n == 1:
    print("1")
else:
    for i in range(2, n):
        a = (dp[-1] + dp[-2]) % 15746
        dp.append(a)

    print(dp[-1])


