# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math


def ableToMakeSquare(n, M, N):
    needSquare = n * n

    if n % 2 == 0:
        # 짝수 개
        needSquare = needSquare - N * 4
        if needSquare == 0:
            return True
        else:
            if needSquare - M <= 0:
                return True
            else:
                return False

    else:
        # 홀수 개
        needSquare = needSquare - N * 4
        if needSquare - M <= 0:
            return True
        else:
            return False


def solution(M, N):
    if M == 0 and N == 0:
        return 0

    numberOfTiles = M + 4 * N
    ableMax = int(math.sqrt(numberOfTiles))

    for i in range(ableMax, 0, -1):
        if ableToMakeSquare(i, M, N):
            print(ableMax)
            return ableMax





solution(0,0)


