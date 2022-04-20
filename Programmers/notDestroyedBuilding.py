board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]



for skil in skill:
    r1,c1,r2,c2 = skil[1],skil[2],skil[3],skil[4]
    for i in range(r1, r2+1):
        for j in range(c1,c2+1):
            # print(skil[0], r1,c1,r2,c2)
            if skil[0] == 1:
                board[i][j] -= skil[5]
            else:
                board[i][j] += skil[5]

answer = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] > 0:
            answer +=1

print(answer)

