n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

values = []

for i in range(len(info)):
    k = len(info) - i - 1

    if info[i] != 0:
        values.append([k*2 / (info[i] + 1), k])
        # print(k, k*2 / (info[i] + 1))
    else:
        values.append([k / (info[i] + 1), k])


values.sort(reverse= True)
answer = [0] * 11
print(values)
values = [[9.0, 9], [8.0, 8], [7.0, 7], [6.666666666666667, 10], [6.0, 6], [6.0, 5], [6.0, 3], [3.0, 3], [2.0, 2], [1.0, 1], [0.0, 0]]
values.sort(key = lambda x:(-x[0], x[1]))
print(values)


for i in range(len(values)):
    current = values[i]
    tmpK = current[1]
    infoIndex = 11- tmpK - 1

    # print(info[infoIndex], current)

    if n >= info[infoIndex] + 1:
        n = n - info[infoIndex] - 1
        answer[infoIndex] = info[infoIndex] + 1


answer[-1] = answer[-1] + n

sum = 0
for i in range(len(answer)):
    opponent = info[i]
    me = answer[i]

    if opponent != 0 or me != 0:
        if opponent >= me:
            sum += (11 - i - 1)
        else:
            sum -= (11 - i - 1)

if sum >= 0 :
    print("-1")
else:
    print(answer)
