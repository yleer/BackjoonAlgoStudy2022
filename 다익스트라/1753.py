import sys
import heapq

v, e = map(int, sys.stdin.readline().strip().split())
start = int(input())

graph = [[] for i in range(len(v+1))]

# for i in range(v+1):
#     graph.append([])

for i in range(e):
    a,b,c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b,c))
    # start a, destination b, cost 0

distances = [1e9] * (v+1)



def dijskstra(start):
    q = []
    distances[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        curCost, curr  = heapq.heappop(q)
        if distances[curr] < curCost:
            continue

        for nextInfo in graph[curr]:
            cost = curCost + nextInfo[1]

            if cost < distances[nextInfo[0]]:
                distances[nextInfo[0]] = cost
                heapq.heappush(q,(cost,nextInfo[0]))





dijskstra(start)
distances.pop(0)


for d in distances:
    if d == 1e9:
        print("INF")
    else:
        print(d)


