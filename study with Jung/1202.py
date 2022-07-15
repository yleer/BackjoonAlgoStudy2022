import sys
import collections
import heapq

n, k = map(int, sys.stdin.readline().split())


jeweries = []
bags = []

# jew = collections.defaultdict(list)



for i in range(n):
    t1, t2 = map(int, sys.stdin.readline().split())
    jeweries.append([t1,t2])
jeweries.sort(key = lambda x:(-x[1], x[0]))

for i in range(k):
    tmp = int(input())
    bags.append(tmp)

# print(jeweries)
# print(bags)



totalValue = 0

for jery in jeweries:
    for bag in bags:
        if jery[0] <= bag:
            totalValue += jery[1]
            bags.remove(bag)
            break

print(totalValue)







