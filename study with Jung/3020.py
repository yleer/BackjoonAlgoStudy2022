import sys


n, h = map(int, sys.stdin.readline().split())

upToBottom = [0] * (h+1)
bottomToUp = [0] * (h+1)


for i in range(1,(n+1)):
    tmp = int(input())
    if i % 2:
        upToBottom[tmp] += 1
    else:
        bottomToUp[h - tmp + 1] += 1

for i in range(1, h + 1):
    bottomToUp[i] += bottomToUp[i - 1]

for i in range(h-1,-1,-1):
    upToBottom[i] += upToBottom[i+1]

result = [0] * (h+1)

for i in range(1,h+1):
    result[i] = bottomToUp[i] + upToBottom[i]


result = result[1:]
answ = min(result)
print(answ, result.count(answ))

