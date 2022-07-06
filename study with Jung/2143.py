import sys, bisect

t = int(input())
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))


arr = []
bArr = []
for i in range(0,len(a)-1):
    for j in range(i, len(a)):
        arr.append(sum(a[i:j+1]))

for i in range(0,len(b)-1):
    for j in range(i, len(b)):
        # bC[sum(b[i:j + 1])] += 1
        bArr.append(sum(b[i:j + 1]))

# aC[a[-1]] += 1
# bC[b[-1]] += 1

arr.append(a[-1])
bArr.append(b[-1])


bArr.sort()


answer = 0
cnt = 0
for i in arr:
    diff = t - i
    idx = bisect.bisect_left(bArr, diff)
    if idx >= len(bArr):
        continue
    # 조합의 합이 같은 경우가 있을 수 있기 때문에 그 인덱스의 차이를 구해준다.
    idx_right = bisect.bisect_right(bArr, diff)
    if bArr[idx] == diff:
        cnt += idx_right - idx

print(cnt)