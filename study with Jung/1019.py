n = 543212345

arr = [0] * 10

print(arr)

for i in range(n+1):
    char = str(i)
    # print(char)
    for c in char:
        if c == '0':
            arr[0] = arr[0] + 1
        elif c == '1':
            arr[1] = arr[1] + 1
        elif c == '2':
            arr[2] = arr[2] + 1
        elif c == '3':
            arr[3] = arr[3] + 1
        elif c == '4':
            arr[4] = arr[4] + 1
        elif c == '5':
            arr[5] = arr[5] + 1
        elif c == '6':
            arr[6] = arr[6] + 1
        elif c == '7':
            arr[7] = arr[7] + 1
        elif c == '8':
            arr[8] = arr[8] + 1
        else:
            arr[9] = arr[9] + 1
print(arr)