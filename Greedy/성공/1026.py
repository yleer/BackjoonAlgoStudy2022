import sys

n = int(input())

a = []
b = []

for i in range(2):
    if i == 0 :
        a = list(map(int, sys.stdin.readline().strip().split()))
    else :
        b = list(map(int, sys.stdin.readline().strip().split()))


# b_set = sorted(b)
# b_id = []
# for i in b:
#     b_id.append(b_set.index(i))
#

a.sort()
b.sort(reverse=True)
sum = 0

for i in range(n):
    t = a[i] * b[i]
    sum = t + sum
print(sum)

