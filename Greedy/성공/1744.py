import sys

input = sys.stdin.readline
n = int(input())

arr = []
for i in range(n):
    t = int(input())
    arr.append(t)


arr.sort()

negativeNums = []
positiveNums = []
numsOfzros = 0
numsOfOnes = 0
totalSum = 0
for num in arr:
    if num < 0:
        negativeNums.append(num)
    elif num == 0:
        numsOfzros += 1
    elif num == 1:
        numsOfOnes += 1
    else:
        positiveNums.append(num)



negativeNums.sort()
positiveNums.sort()


negativeSum = 0
while len(negativeNums) >= 2:
    negativeSum += negativeNums.pop(0) * negativeNums.pop(0)

if len(negativeNums) == 1:
    if numsOfzros > 0:
        pass
    else:
        negativeSum += negativeNums[0]


print(negativeSum, negativeNums[0])



positiveNums.reverse()
postiveSum = 0
while len(positiveNums) >= 2:
    sum = positiveNums.pop(0) * positiveNums.pop(0)
    postiveSum += sum
if len(positiveNums) == 1:
    postiveSum += positiveNums[0]

result = negativeSum + postiveSum + numsOfOnes

print(negativeSum, postiveSum, numsOfOnes, numsOfzros)
print(result)










