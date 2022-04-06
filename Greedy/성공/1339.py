import collections

n = int(input())

mapping = collections.defaultdict(int)
for i in range(n):
    tmp = input()
    for i in range(len(tmp)):
        k = len(tmp) - 1 - i
        mapping[tmp[i]] = mapping[tmp[i]] + pow(10,k)

a = sorted(mapping.items(), key = lambda item: item[1], reverse= True)

# print(a)
count = 9
sum = 0
for index in range(len(a)):
    curr = a[index]
    sum += curr[1] * count
    count = count - 1

print(sum)