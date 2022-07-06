
rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate(rc, row,column):
    queries = [[0, 0, len(rc)-1, len(rc[0])-1]]  # x1, y1, x2, y2 (x1, y1 부터 x2, y2 범위)

    cnt = 0

    for i in range(row):
        for j in range(column):
            cnt += 1
            rc[i][j] = cnt

    for t, l, b, r in queries:
        top, left, bottom, right = t - 1, l - 1, b - 1, r - 1  # index 계산을 편하게 하기 위해서 빼준다.
        temp = rc[top][left]

        for k in range(top, bottom):  # 1번
            rc[k][left] = rc[k + 1][left]

        for k in range(left, right):  # 2번
            rc[bottom][k] = rc[bottom][k + 1]

        for k in range(bottom, top, -1):  # 3번
            rc[k][right] = rc[k - 1][right]

        for k in range(right, left, -1):  # 4번
            rc[top][k] = rc[top][k - 1]

        rc[top][left + 1] = temp  # temp 넣기

        for i in rc:
            print(*i, end=' ')
            print()

rotate(rc,len(rc), len(rc[0]))