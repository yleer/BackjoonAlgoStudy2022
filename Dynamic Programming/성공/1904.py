import sys
input = sys.stdin.readline
n = int(input())

dp = [1,2]

for i in range(2, n):
    a = (dp[-1] + dp[-2]) % 15746
    dp.append(a)


if n == 1:
    print("1")

print(dp[-1])