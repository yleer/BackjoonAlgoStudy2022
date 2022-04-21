board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill =[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]


changedBoard = []

for i in range(len(board)):
    t = []
    for j in range(len(board[0])):
        t.append(0)
    changedBoard.append(t)


for skil in skill:
    r1,c1,r2,c2 = skil[1],skil[2],skil[3],skil[4]
    (r1,c1)  # 시작 점.

    if skil[0] == 1:
        # attack
        changedBoard[r1][c1] -= skil[5]
        if r2 + 1 < len(changedBoard):
            changedBoard[r2+1][c1] += skil[5]

        if c2 + 1 < len(changedBoard[0]):
            changedBoard[r1][c2+1] += skil[5]

        if c2 + 1 < len(changedBoard[0]) and r2 + 1 < len(changedBoard):
            changedBoard[r2 + 1][c2 + 1] -= skil[5]

    else:
        # save
        changedBoard[r1][c1] += skil[5]
        if r2 + 1 < len(changedBoard):
            changedBoard[r2 + 1][c1] -= skil[5]

        if c2 + 1 < len(changedBoard[0]):
            changedBoard[r1][c2 + 1] -= skil[5]

        if c2 + 1 < len(changedBoard[0]) and r2 + 1 < len(changedBoard):
            changedBoard[r2 + 1][c2 + 1] += skil[5]


print(board)
print(changedBoard)


for i in range(len(board)):
    addUp = 0
    for j in range(len(board[0])):
        cur = changedBoard[i][j]
        changedBoard[i][j] += addUp
        addUp += cur

for i in range(len(board[0])):
    addUp = 0
    for j in range(len(board)):
        cur = changedBoard[j][i]
        changedBoard[j][i] += addUp
        addUp += cur


print(changedBoard)

answer = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] + changedBoard[i][j] > 0:
            answer +=1


print(answer)






# for skil in skill:
#     r1,c1,r2,c2 = skil[1],skil[2],skil[3],skil[4]
#     for i in range(r1, r2+1):
#         for j in range(c1,c2+1):
#             # print(skil[0], r1,c1,r2,c2)
#             if skil[0] == 1:
#                 board[i][j] -= skil[5]
#             else:
#                 board[i][j] += skil[5]
#
# answer = 0
# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if board[i][j] > 0:
#             answer +=1
#
# print(answer)
#
