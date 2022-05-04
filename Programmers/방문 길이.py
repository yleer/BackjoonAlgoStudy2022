# answer = 0
# dirs = "ULURRDLLU"
# arr = [[0 for _ in range(11) ]for _ in range(11)]
#
#
# # print(arr)
# curr = [5, 5]
# # arr[5][5] = 4
#
# se = set()
#
# for dir in dirs:
#     x, y = curr
#
#
#     if dir == "U":
#         if y - 1 >= 0:
#             if arr[x][y] == 0 or (arr[x][y] == 1 and arr[x][y-1] == 0):
#                 se.add((x,y,x,y-1))
#             curr = [x, y - 1]
#
#     elif dir == "D":
#         if y + 1 <= 10:
#             if arr[x][y ] == 0 or (arr[x][y] == 1 and arr[x][y+1] == 0):
#                 se.add((x,y,x,y+1))
#             curr = [x, y + 1]
#     elif dir == "L":
#
#         if x - 1 >= 0:
#             # print("asdf", arr[x-1][y], x-1, y)
#             if arr[x ][y] == 0 or (arr[x][y] == 1 and arr[x-1][y] == 0):
#                 # print("z")
#                 se.add((x,y,x-1,y))
#             curr = [x - 1, y]
#     elif dir == "R":
#         if x + 1 <= 10:
#             if arr[x][y] == 0 or (arr[x][y] == 1 and arr[x][y+1] == 0):
#                 # arr[x + 1][y] = 1
#                 se.add((x, y, x + 1, y))
#             curr = [x + 1, y]
#
#
# print(len(se))


a = 3

if 2 <= a <= 4:
    print("gg")