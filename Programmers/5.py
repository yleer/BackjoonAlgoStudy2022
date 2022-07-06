rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate(r, rows, columns):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x1 = 1
    y1 = 1
    x2 = rows
    y2 = columns
    way = 0
    x = x1 - 1
    y = y1 - 1
    curr = r[x][y]

    while way < 4:
        nx, ny = x + dxy[way][0], y + dxy[way][1]
        if x1 - 1 <= nx <= x2 - 1 and y1 - 1 <= ny <= y2 - 1:
            curr, r[nx][ny] = r[nx][ny], curr
            x, y = nx, ny
        else: way += 1


operations = ["Rotate", "ShiftRow"]



for op in operations:
    if op[0] == "R":
        rotate(rc, len(rc), len(rc[0]))
    else:
        rc = [rc[-1]] + rc[:-1]




print(rc)