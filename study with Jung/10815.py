import sys
import collections

n = int(input())
have = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

dic = collections.defaultdict(int)

for h in have:
    dic[h] = 1

answer = []

for i in range(len(check)):
    if dic[check[i]] == 1:
        answer.append(1)
    else:
        answer.append(0)

for an in answer:
    print(an,end=" ")
