import  sys

n = int(input())
a = list(map(int, sys.stdin.readline().strip().split()))

# dp = [[a[0]]]
# for i in range(1,n):
#     currentNum = a[i]
#
#     dp.append([currentNum])
#     for ar in dp:
#         if ar[-1] < currentNum:
#             ar.append(currentNum)
#
# arrayLen = []
# for i in dp:
#     arrayLen.append(len(i))
# print(max(arrayLen))
# print(dp)

dp = [0] * n

dp[n-1] = 1

for i in range(n-2, -1, -1):
    tmp = []
    for j in range(i+1, n):
        if a[i] < a[j]:
            tmp.append(dp[j] + 1)
    if len(tmp) != 0:
        dp[i] = max(tmp)
    else:
        dp[i] = 1


print(max(dp))