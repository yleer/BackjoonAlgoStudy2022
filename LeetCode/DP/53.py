# nums = [-2,1,-3,4,-1,2,1,-5,4]
#
# nums = [5,4,-1,7,8]
import sys
nums = [1]

n = int(input())
nums = map(int, sys.stdin.readline().strip().split())


dp = [[nums[0]]]



maxNum = [nums[0]]
for i in range(len(nums)):
    if i == 0:
        pass
    else:
        last = dp[-1]
        k = []
        k.append(nums[i])

        for item in last:
            k.append(item + nums[i])
        dp.append([max(k)])
        maxNum.append(max(k))

#
# print(dp)
# print(maxNum)

print(max(maxNum))