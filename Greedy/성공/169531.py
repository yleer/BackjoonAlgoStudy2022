import sys

n, w = list(map(int, sys.stdin.readline().strip().split()))


arr = [[n, 1]]

while True:

    if len(arr) == 0 :
        print("-1")
        break
    curr = arr.pop()
    twoTimes, c1 = curr[0] * 2, curr[1] + 1
    plusedOne, c2 = int(str(curr[0]) + "1"), curr[1] + 1


    if twoTimes == w:
        print(c1)
        break
    elif twoTimes < w:
        arr.append([twoTimes, c1])


    if plusedOne == w:
        print(c2)
        break
    elif plusedOne < w:
        arr.append([plusedOne, c2])







