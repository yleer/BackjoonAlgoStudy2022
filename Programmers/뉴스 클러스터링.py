import collections

str1 = "handshake"
str2 = "shake hands"

dic = collections.defaultdict(list)

str1 = str1.lower()
str2 = str2.lower()

for index in range(len(str1) - 1):
    if str1[index].isalpha() and str1[index+1].isalpha():
        combo = str1[index] + str1[index+1]
        if len(dic[combo]) < 2:
            dic[combo] = [1,0]
        else:
            dic[combo][0] += 1


for index in range(len(str2) - 1):
    if str2[index].isalpha() and str2[index+1].isalpha():
        combo = str2[index] + str2[index + 1]
        if len(dic[combo]) < 2:
            dic[combo] = [0, 1]
        else:
            dic[combo][1] += 1

print(dic)


up = 0
down = 0
for key, value in dic.items():
    first, second = value

    if first == 0:
        down += second

    if second == 0:
        down += first


    if first != 0 and second != 0:
        up += min(first,second)
        down += max(first,second)


# print(up)
# print(down)
result = up / down * 65536
result = int(result)
print(result)