n = int(input())

staris = [0]
for i in range(n):
    tmp = int(input())
    staris.append(tmp)
#
#
# print(staris)
dp = [0, staris[0], staris[1] + staris[0]]

print(dp)
for i in range(len(staris)+1):
    if i == 0 or i == 1 or i == 2 :
        pass
    else:
        a = dp[i-2] + staris[i]
        b = dp[i-1] + dp[i-3] + staris[i]
        dp.append(max(a,b))


print(dp)

# import sys
# read = sys.stdin.readline
#
# n = int(read())
# stairs = [0] + [int(read()) for _ in range(n)] + [0]
# print(stairs)
# cache = [0] * (n+2)
# cache[1] = staris[1]
# cache[2] = cache[1] + staris[2]
#
# print(cache)
#
# for i in range(3, n+1):
#     cache[i] = max(cache[i-2], cache[i-3] + staris[i-1]) + staris[i]
# print(cache[n])