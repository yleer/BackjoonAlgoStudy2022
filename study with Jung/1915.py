import sys

n, m = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    c = list(map(str, sys.stdin.readline().split()))
    t = []
    for i in range(len(c[0])):

        t.append(c[0][i])
    arr.append(t)

def checkSquare(x,y):

    maxLen = min(n-x, m-y)
    maxArea = 1

    t = False
    for i in range(1, maxLen):
        # t = False
        for j in range(x,x+i+1):
            if t:
                t = False
                break
            for k in range(y,y+i+1):
                if (x == j and arr[j][k] == "1") or (y == k and arr[j][k] == '1') or\
                        (x + i == j and arr[j][k] == "1") or (y + i == k and arr[j][k] == '1'):
                    pass
                else:
                    t = True
                    i = 0
                    break
        #
        # print(x,y,i)
        maxArea = (i + 1) * (i + 1)
    return maxArea


answer = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == "1":
            answer = max(checkSquare(i,j),answer)

print(answer)
