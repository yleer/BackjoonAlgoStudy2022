import sys
n = int(input())
answers = []
z = []
for i in range(n):

    m = int(input())
    first = list(map(int, sys.stdin.readline().strip().split()))
    second = list(map(int, sys.stdin.readline().strip().split()))

    first.insert(0,0)
    second.insert(0,0)
    dp = [0] * (m + 1)


    dp[0] = [0,5]
    if first[1] > second[1]:
        dp[1] = [first[1],1]
    elif first[1] < second[1]:
        dp[1] = [second[1], 2]
    elif first[1] == second[1]:
        dp[1] = [first[1], 3]

    # value, index
    for j in range(2, m+1):

        # if first[j] != second[j]:
            a = 0
            b = 0
            needToAvoid = dp[j-1][1]

            if needToAvoid == 1:
                a = [dp[j-1][0] + second[j],2]
            elif needToAvoid == 2:
                a = [dp[j-1][0] + first[j],1]
            elif needToAvoid == 3:
                if first[j] > second[j]:
                    a = [dp[j-1][0] + first[j],1]
                else:
                    a = [dp[j - 1][0] + second[j], 2]


            if first[j] > second[j]:
                b = [dp[j-2][0] + first[j], 1]
            else:
                b = [dp[j - 2][0] + second[j], 2]


            if a[0] > b[0]:
                dp[j] = a
            else:
                dp[j] = b
        # else:
        #     dp[j] = [dp[j-1][0] + first[j],3]

    z.append(dp)
    answers.append(dp[-1][0])

print(z)
# print(answers)

for item in answers:
    print(item)