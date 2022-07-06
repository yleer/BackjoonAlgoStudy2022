import sys
import collections

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    line = input()
    arr.append(line)
visited = [[0 for _ in range(m)] for _ in range(n)]

# print(visited)
loc = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x,y):
    q = collections.deque()
    q.append((x,y))

    while q:
        a,b = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b] + 1

        for move in loc:
            nx, ny = a + move[0], b + move[1]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and arr[nx][ny] == '1':
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx,ny))




print(bfs(0,0))

