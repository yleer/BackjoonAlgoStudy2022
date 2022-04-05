import sys




count = int(input())
totalArray = []
for i in range(count):
    m = int(input())
    arr = []
    for i in range(m):
        n, w = list(map(int, sys.stdin.readline().strip().split()))
        arr.append([n, w])

    totalArray.append(arr)


answers = []
for arr in totalArray:
    arr.sort()

    answer = 0
    best = arr[0]
    for i in range(1,len(arr)):
        curr = arr[i]

        if best[0] < curr[0] and best[1] < curr[1]:
            answer += 1
        elif best[0] > curr[0] and best[1] < curr[1]:
            best = [best[0], best[1]]
        elif best[0] < curr[0] and best[1] > curr[1]:
            best = [curr[0], curr[1]]
        else:
            continue

    answers.append(answer)


# print(totalArray, answers[1])

for i in range(count):

    print(len(totalArray[i]) - answers[i])