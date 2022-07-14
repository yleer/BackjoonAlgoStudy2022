#
# li = []
#
#
# def binarySearch(target, arr):
#     mid = int(len(arr) / 2)
#
#     if len(arr) == 1:
#         if arr[0] != target:
#             return -1
#
#     if target > arr[mid]:
#         return binarySearch(target, arr[mid:])
#     elif target < arr[mid]:
#         return binarySearch(target, arr[:mid])
#     else:
#         return mid
#
#
#

a = [1,2,4,5] + [3,6]
print(a)
