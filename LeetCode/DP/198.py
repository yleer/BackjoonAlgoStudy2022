nums = [2,7,9,3,1]

dp = [nums[0], nums[1], nums[2] + nums[0]]

for i in range(3,len(nums)):
    current = nums[i]
    dp.append(max(dp[i - 2], dp[i - 3]) + current)


print(max(dp))

