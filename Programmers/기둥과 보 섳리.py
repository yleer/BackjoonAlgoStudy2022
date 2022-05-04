n = 5
n = n + 1
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]


arr = [[0 for _ in range(n)] for _ in range(n)]

# print(arr)


arr[0][0] = 2
for i in range(n):
    for j in range(n):
        print(arr[i][j], end= " ")
    print()





