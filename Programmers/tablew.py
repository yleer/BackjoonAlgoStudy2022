n = 8
k = 6
cmd = 	["C","C","C","Z","C"]

ar = []

for i in range(n):
    ar.append(i)


erased = []
for i in range(len(cmd)):

    command = cmd[i]

    print(command, ar, k)
    if command[0] == "U":
        k = k - int(command[2:])
    elif command[0] == "D":
        k = k + int(command[2:])
    elif command[0] == "C":
        if k == len(ar) - 1:
            erased.append([ar[k], k])
            ar = ar[:k]
            k = k-1
        else:

            ar = ar[:k] + ar[k + 1:]
            erased.append([ar[k] - 1, k])

    elif command[0] == "Z":
        recovery = erased.pop()
        if recovery[1] <= k:
            ar.insert(recovery[1], recovery[0])
            k = k + 1
        else:
            ar.insert(recovery[1], recovery[0])






print(ar)

answer = ""
for i in range(n):
    if i in ar:
        answer = answer +"O"
    else:
        answer = answer + "X"

print(answer)

