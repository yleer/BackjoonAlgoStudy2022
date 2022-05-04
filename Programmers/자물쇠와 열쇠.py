# import  copy
# def rotateToRight(arr):
#     t = []
#     for i in range(len(arr[0])):
#         tmp =[]
#         for j in range(len(arr[0])-1, -1, -1):
#             tmp.append(arr[j][i])
#         t.append(tmp)
#
#     arr = t
#     return arr
#
# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
#
# offset = len(key) - 1
# arr = [[0 for _ in range(len(lock) + offset * 2)] for _ in range(len(lock) + offset * 2)]
# # 정 중앙에 lock 삽입
# for i in range(len(lock)):
#     for j in range(len(lock)):
#         arr[i+offset][j+offset] = lock[i][j]
# dict()
#
# for r in range(len(lock) + offset ):
#     for c in range(len(lock) + offset ):
#
#         keyCopy = copy.deepcopy(key)
#
#         for _ in range(4):
#             copyOfArr = copy.deepcopy(arr)
#             checking = False
#             keyCopy = rotateToRight(keyCopy)
#
#
#             ## copyOfArr에 key 값 더하기
#             for i in range(len(keyCopy)):
#                 for j in range(len(keyCopy[0])):
#                     copyOfArr[r+i][c+j] += keyCopy[i][j]
#
#             # 중앙 부분 해결 되었나 확인하기
#             for i in range(len(lock)):
#                 if checking:
#                     break
#                 for j in range(len(lock[0])):
#                     if copyOfArr[offset+i][offset+j] != 1:
#                         checking = True
#                         break
#
#             if checking == False:
#                 print("succes")
#                 # 더해진거 출력하기
#                 for i in range(len(copyOfArr)):
#                     for j in range(len(copyOfArr)):
#                         print(copyOfArr[i][j], end=" ")
#                     print()
#
#
#
#
#
#
#
#
#

import  collections

a = dict()
a[2] =[]
