n = int(input())

dp = [[1,0],[0,1]]
for i in range(2,n):
    curr = dp[-1]
    numberOfOnes = curr[0]
    numberOfZeros = curr[1]


    nextOnes = numberOfZeros
    nextZeros = numberOfOnes + numberOfZeros
    next = [nextOnes,nextZeros]
    dp.append(next)


print(sum(dp[-1]))