n = int(input())

array = [0] * (n + 1)

for i in range(1,n + 1):

    if i == 1:
        array[i] = 0
    elif i == 2 or i == 3 :
        array[i] = 1

    else:
        tmp = []
        if i % 3 == 0:
            tmp.append(array[int(i / 3)])
        if i % 2 == 0:
            tmp.append(array[int(i / 2)])
        tmp.append(array[i- 1])

        # print(i, tmp)

        tmp.sort()
        array[i] = tmp[0] + 1


print(array[-1])

