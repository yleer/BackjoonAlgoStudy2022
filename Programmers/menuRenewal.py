import collections
import itertools
orders = ["XYZ", "XWY", "WXA"]

course = [2,3,4]

dic = collections.defaultdict(int)


for order in orders:
    b = list(order)
    for cour in course:
        a = list(itertools.combinations(b,cour))
        for item in a:
            # print(item)
            # p =
            # print("".join(item))
            # p = sorted()
            # print("".join(item))
            qq = "".join(item)


            dic["".join(sorted(qq))] += 1


answers = []
print(dic)
for co in course:
    tmp = []
    for key, value in dic.items():
        if len(key) == co:
            current = [key, value]
            if len(tmp) == 0:
                tmp.append(current)
            else:
                prev = tmp[-1]
                # print(tmp, prev)
                if current[1] > prev[1]:
                    tmp = [current]
                elif current[1] == prev[1]:
                    tmp.append(current)

    answers += tmp

# print(answers)
k = []
for an in answers:
    if an[1] != 1:
        k.append(an)
k.sort()
answer = []
for z in k:
    answer.append(z[0])

print(answer)

