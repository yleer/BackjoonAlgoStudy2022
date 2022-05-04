A = [5,1,3,7]
B = [2,2,6,8]

answer = 0

A.sort()
B.sort()

aCounter = 0
for i in range(len(A)):
    if i + aCounter < 0:
        break
    if B[i] > A[i + aCounter]:
        answer += 1
    else:
        aCounter -= 1


print(answer)