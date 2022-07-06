import sys

n, m = map(int, sys.stdin.readline().split())

rounds = []
for i in range(m):
    round = list(map(int, sys.stdin.readline().split()))
    rounds.append(round)


wins = [set() for _ in range(n)]
loses = [set() for _ in range(n)]


for i in range(len(rounds)):
    wins[rounds[i][1]-1].add(rounds[i][0])
    loses[rounds[i][0]-1].add(rounds[i][1])


for i in range(len(wins)):
    listedSet = list(wins[i])
    for j in range(len(listedSet)):
        wins[i] = wins[listedSet[j]-1].union(wins[i])

for i in range(len(wins)):
    listedSet = list(wins[i])
    for j in range(len(listedSet)):
        wins[i] = wins[listedSet[j]-1].union(wins[i])


for i in range(len(loses)):
    listedSet = list(loses[i])
    for j in range(len(listedSet)):
        loses[i] = loses[listedSet[j]-1].union(loses[i])

for i in range(len(loses)):
    listedSet = list(loses[i])
    for j in range(len(listedSet)):
        loses[i] = loses[listedSet[j]-1].union(loses[i])

count = 0

for i in range(len(wins)):
    if len(wins[i]) + len(loses[i]) == n-1:
        count += 1

print(count)



