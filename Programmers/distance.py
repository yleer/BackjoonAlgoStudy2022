arr =  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]
# x(row) y(col)
def checkDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

seats = []
partitions = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == "P":
            seats.append([i,j])
        elif arr[i][j] == "X":
            partitions.append([i,j])

def checkNearBy(arr, seats) :
    for i in range(len(seats)):
        for j in range(i + 1, len(seats)):
            dis = checkDistance(seats[i], seats[j])
            if dis > 2:
                pass
            elif dis == 1:
                return 0
            elif dis == 2:
                if seats[i][0] == seats[j][0]:
                    # same row
                    if arr[seats[i][0]][int(seats[i][1] + 1)] != "X":
                        return 0
                elif seats[i][1] == seats[j][1]:
                    if arr[int(seats[i][0] + 1)][int(seats[i][1])] != "X":
                        return 0
                else:
                    if seats[i][0] + 1 < 5  and seats[i][1] + 1 < 5:
                        if arr[seats[i][0] + 1][seats[i][1]] != "X" or arr[seats[i][0]][ seats[i][1] + 1] != "X":
                            return 0

                        if arr[seats[i][0]][seats[i][1] -1 ] != "X" or arr[seats[i][0] + 1][seats[i][1]] != "X" :
                            return 0


                    if seats[i][1] + 1 == seats[j][1]:
                        if arr[seats[i][0]][seats[i][1] + 1] != "X" or arr[seats[i][0]+1][seats[i][1]] != "X":
                            return 0
                    else:
                        if arr[seats[i][0]][seats[i][1] - 1] !="X" or arr[seats[i][0]+1][seats[i][1]] != "X":
                            return 0



    return 1

a = checkNearBy(arr,seats)
print(a)