import collections
import copy
import heapq


fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
n = 6
s = 4
a = 6
b = 2

graph = []
distances = [1e9] * (n+1)

for i in range(n+1):
    graph.append([])


print(graph)

for far in fares:
    graph[far[0]].append((far[1], far[2]))
    graph[far[1]].append((far[0], far[2]))

print(graph)

def dijskstra(start):
    q = []
    distances[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        curCost, curr = heapq.heappop(q)
        if distances[curr] < curCost:
            continue

        for nextInfo in graph[curr]:
            cost = curCost + nextInfo[1]

            if cost < distances[nextInfo[0]]:
                distances[nextInfo[0]] = cost
                heapq.heappush(q,(cost,nextInfo[0]))


def findShortest(start, aDst, bDst):


dijskstra(s)

print(distances)



