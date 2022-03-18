import sys

n, w = map(int, sys.stdin.readline().strip().split())

usingBytes = map(int, sys.stdin.readline().strip().split())
usingBytes = list(usingBytes)

costs = map(int, sys.stdin.readline().strip().split())
costs = list(costs)


print(n,w)
print(usingBytes)
print(costs)

sizePerCost = []

for i in range(n):
     sizePerCost.append(costs[i] / usingBytes[i])

print(sizePerCost)