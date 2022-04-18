n = 8
k = 2
cmd = 	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]


class TableNode:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None


nodeArray = []

for i in range(n):
    nodeArray.append(TableNode())

nodeArray[0].next = nodeArray[1]
nodeArray[-1].prev = nodeArray[-1]
for i in range(1,n-1):
    nodeArray[i].prev = nodeArray[i-1]
    nodeArray[i].next = nodeArray[i+1]


curr = nodeArray[k]
myStack = []


for command in cmd:
    if command[0] == "U":
        x = int(command[2:])
        for _ in range(x):
            curr = curr.prev
    elif command[0] == "D":
        x = int(command[2:])
        for _ in range(x):
            curr = curr.next
    elif command[0] == "C":
        myStack.append(curr)
        curr.removed = True
        prev = curr.prev
        after = curr.next


        if prev:
            prev.next = after
        if after:
            after.prev = prev
        else:
            prev.next = None
            curr = prev


    elif command[0] == "Z":
        poped = myStack.pop()
        poped.removed = False
        before = poped.prev
        after = poped.next

        if before:
            before.next = poped

        if after:
            after.prev = poped

answer = ""
for i in range(n):
    if nodeArray[i].removed:
        answer += "X"
    else:
        answer += "O"

print(answer)
# erased = []
# for i in range(len(cmd)):
#     command = cmd[i]
#     if command[0] == "U":
# #         k = k - int(command[2:])
# #     elif command[0] == "D":
# #         k = k + int(command[2:])
# #     elif command[0] == "C":
# #         if k == len(ar) - 1:
# #             erased.append([ar[k], k])
# #             ar = ar[:k]
# #             k = k-1
# #         else:
# #             ar = ar[:k] + ar[k + 1:]
# #             erased.append([ar[k] - 1, k])
# #
# #     elif command[0] == "Z":
#         recovery = erased.pop()
#         if recovery[1] <= k:
#             # ar.insert(recovery[1], recovery[0])
#
#             ar = ar[:recovery[0]] + [recovery[1]] + ar[recovery[0]:]
#
#
#             k = k + 1
#         else:
#             # ar.insert(recovery[1], recovery[0])
#             ar = ar[:recovery[0]] + [recovery[1]] + ar[recovery[0]:]

# print(ar)
#
# answer = ""
# for i in range(n):
#     if i in ar:
#         answer = answer +"O"
#     else:
#         answer = answer + "X"
#
# print(answer)

