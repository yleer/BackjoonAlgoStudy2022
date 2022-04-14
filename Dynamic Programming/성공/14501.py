import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    time, money = map(int, sys.stdin.readline().strip().split())

    arr.append([time,money])

arr.insert(0,0)
dp = [0] * (n+1)

for i in range(1, n+1):

    for j in range(1, i+1):
        needTime, earnMoney = arr[j]


