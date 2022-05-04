# import math
#
#
# math.comb()
# math.pow()
# math.factorial()
#
#
# def is_prime_number(x):
#     if x == 1:
#          return False
#     for i in range(2,int(x**0.5)+1):
#         if x % i == 0:
#             return False # 소수가 아님
#     return True # 소수임


a = [1,6]

b= [1,6,3]

c = all(elem in b for elem in a)
print(c)
