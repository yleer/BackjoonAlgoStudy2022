import sys
import  math



def combination(m,n):

    a = math.factorial(m)
    b = math.factorial(m - n) * math.factorial(n)
    return  a / b

input = sys.stdin.readline
n = int(input())

answer = []
for i in range(n):
    n, m = map(int, sys.stdin.readline().strip().split())
    # combination()
    a = math.comb(m,n)
    answer.append(a)


for a in answer:
    print(a)

    # mCn 하면 됨



