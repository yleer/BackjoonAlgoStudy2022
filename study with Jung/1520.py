# import sys
# import collections
# import copy
#
#
# arr = collections.deque()
# n, m = map(int, sys.stdin.readline().strip().split())
#
#
# tm = [-1] * (m +2)
# arr.append(tm)
# for i in range(n):
#     t = collections.deque(map(int, sys.stdin.readline().strip().split()))
#     t.appendleft(-1)
#     t.append(-1)
#     arr.append(t)
# arr.append(tm)
#
# start = (1,1)
#
# possible = [[start]]
# answer = 0
#
# answers = []
# while possible:
#     current = possible.pop()
#     current_position = current[-1]
#
#
#     if (current_position[0],current_position[1]) in answers:
#         answer += 1
#     else:
#         # down
#
#         if arr[current_position[0] + 1][current_position[1]] < arr[current_position[0]][current_position[1]]:
#             if current_position[0]+1 == n and current_position[1] == m :
#                 answers = answers + current + [(current_position[0]+1,current_position[1])]
#                 answer += 1
#             elif arr[current_position[0] + 1][current_position[1]] == -1:
#                 pass
#             else:
#                 c = copy.deepcopy(current)
#                 c.append((current_position[0] + 1, current_position[1]))
#                 possible.append(c)
#         else:
#             pass
#         # up
#         if arr[current_position[0] - 1][current_position[1]] < arr[current_position[0]][current_position[1]]:
#             if current_position[0]-1 == n and current_position[1] == m:
#                 answers = answers + current + [(current_position[0] - 1, current_position[1])]
#                 answer += 1
#             elif arr[current_position[0] - 1][current_position[1]] == -1:
#                 pass
#             else:
#                 c = copy.deepcopy(current)
#                 c.append((current_position[0] - 1, current_position[1]))
#                 possible.append(c)
#         else:
#             pass
#
#         # left
#         if arr[current_position[0]][current_position[1] - 1] < arr[current_position[0]][current_position[1]]:
#             if current_position[0] == n and current_position[1]-1 == m :
#                 answers = answers + current + [(current_position[0], current_position[1] -1)]
#                 answer += 1
#             elif arr[current_position[0]][current_position[1] -1] == -1:
#                 pass
#             else:
#                 c = copy.deepcopy(current)
#                 c.append((current_position[0], current_position[1]-1))
#                 possible.append(c)
#         else:
#             pass
#
#         # right
#         if arr[current_position[0]][current_position[1] + 1] < arr[current_position[0]][current_position[1]]:
#             if current_position[0] == n and current_position[1] + 1 == m:
#                 answers = answers + current + [(current_position[0], current_position[1] + 1)]
#                 answer += 1
#             elif arr[current_position[0]][current_position[1]+1] == -1:
#                 pass
#             else:
#                 c = copy.deepcopy(current)
#                 c.append((current_position[0], current_position[1] + 1))
#                 possible.append(c)
#         else:
#             pass
#
#
# # print(answers)
# print(answer)
#
#
#

import sys

sys.setrecursionlimit(10**6)


n, m = map(int, sys.stdin.readline().split())
height = []
for _ in range(n):
    height.append(list(map(int, sys.stdin.readline().split())))
visited = [[-1 for _ in range(m)] for __ in range(n)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def search(x,y):
    if x == n-1 and y == m-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if height[nx][ny] < height[x][y]:
                visited[x][y] += search(nx, ny)

    return visited[x][y]


print(search(0, 0))
# print(visited)
