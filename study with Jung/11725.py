import sys
import collections

n = int(input())

tree = collections.defaultdict(list)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    tree[a].append(b)
    tree[b].append(a)


visited = []
while visited != n-1:

    pass


