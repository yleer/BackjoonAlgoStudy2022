import sys
import collections

v = int(input())

tree = collections.defaultdict(list)

for i in range(v):
    a = list(map(str, sys.stdin.readline().split()))
    for j in range(1,len((a))-1):
        if j % 2 == 1 and a[j] != -1:
            tree[a[0]].append([a[j], a[j+1]])

largest = -1
node = -1
def bfs(current, visited, cost):
    global largest, node
    nextLocations = tree[current]

    for nx in nextLocations:
        if nx[0] not in visited:
            bfs(nx[0], visited + [current], cost + int(nx[1]))


    if largest < cost:
        largest = cost
        node = current
    return (current, cost)


bfs("1",[],0)

largest = 0

bfs(str(node),[],0)

print(largest)