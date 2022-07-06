import sys
import collections

n, m = map(int, sys.stdin.readline().split())
answers = []
arr = []
for _ in range(n):
    line = input()
    arr.append(line)


loc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


def bfs(x,y,z):
    queue = collections.deque()
    queue.append((x, y, z))

    while queue:
        a,b,c = queue.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]

        for move in loc:
            nx, ny = a + move[0], b + move[1]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == '1' and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx,ny,1))
                elif arr[nx][ny] == '0' and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    queue.append((nx,ny,c))

    return -1
print(bfs(0,0,0))






# def search(crushed, history):
#     global answers
#     history_copy = copy.copy(history)
#     current = history_copy[-1]
#
#     # print(current, crushed)
#
#     if current[0] == n - 1 and current[1] == m - 1:
#         answers.append(len(history_copy))
#         # print(history_copy)
#         return
#
#     if crushed == 0:
#         for i in loc:
#             nx = current[0] + i[0]
#             ny = current[1] + i[1]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if arr[nx][ny] == '0':
#                     if (nx,ny) not in history_copy:
#                         search(crushed, history_copy + [(nx,ny)])
#                 else:
#                     # history_copy.append((nx, ny))
#                     if (nx, ny) not in history_copy:
#                         search(1, history_copy + [(nx,ny)])
#     else:
#         # print("crushd ", current)
#         for i in loc:
#             nx = current[0] + i[0]
#             ny = current[1] + i[1]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if arr[nx][ny] == '0':
#                     if (nx,ny) not in history_copy:
#                         # history_copy.append((nx, ny))
#                         search(crushed, history_copy + [(nx,ny)])
#                 else:
#                     answers.append(-1)
#                     # return -1




