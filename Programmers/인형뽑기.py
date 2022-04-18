board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


stack = []


answer = 0


for move in moves:
    col = move - 1

    for i in range(5):
        if board[i][col] == 0:
            if i == 5-1:
                break
            else:
                continue
        else:
            val = board[i][col]


            if len(stack) > 0 :
                if stack[-1] == val:
                    stack.pop()
                    answer = answer + 2
                else:
                    stack.append(val)
            else:
                stack.append(val)
            board[i][col] = 0
            break



print(answer)



