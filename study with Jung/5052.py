import sys

def check(arr):
    for i in range(len(arr)-1):
        firstLen = len(arr[i])
        if arr[i+1][:firstLen] == arr[i]:
            return False
    return True


t = int(input())
answer = []
for i in range(t):
    tmp = []
    n = int(input())
    for j in range(n):
        a = sys.stdin.readline().strip("\n")
        tmp.append(a)
    tmp.sort()

    if check(tmp):
        answer.append("YES")
    else:
        answer.append("NO")


for item in answer:
    print(item)