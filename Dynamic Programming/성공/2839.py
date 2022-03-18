n = int(input())

array = [0] * (n + 1)


for i in range(len(array)):
    if i == 0 :
        array[i] = -1
    elif i == 1:
        array[i] = -1
    elif i == 2:
        array[i] = -1
    elif i == 3:
        array[i] = 1
    elif i == 4:
        array[i] = -1
    elif i == 5:
        array[i] = 1
    else:
        currentNum = array[i]
        if array[i - 5] == -1:
            if array[i - 3] != -1:
                array[i] = array[i - 3] + 1
            else:
                array[i] = -1
        else:
            array[i] = array[i - 5] + 1

print(array[-1])