import re

info = ["java backend junior pizza 150",
        "java backend junior chicken 80",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "python backend senior chicken 50"
        ]


query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"
         ]


# answer = []
#
# for qu in query:
#     # q = qu.split("and", " ")
#     q = re.split('and |[ ]', qu)
#     new = []
#     # print(q)
#     for i in range(len(q)):
#         if q[i] != "":
#             new.append(q[i])
#
#     ans = 0
#     for inf in info:
#         data = inf.split(" ")
#
#         if new[0] == "-" or new[0] == data[0]:
#             if new[1] == "-" or new[1] == data[1]:
#                 if new[2] == "-" or new[2] == data[2]:
#                     if new[3] == "-" or new[3] == data[3]:
#                         if int(new[4]) <= int(data[4]):
#                             ans += 1
#                         else:
#                             continue
#                     else:
#                         continue
#                 else:
#                     continue
#
#             else:
#                 continue
#         else:
#             continue
#
#
#     answer.append(ans)
#
#
# print(answer)


from itertools import combinations
dic = {
    "-" : 0,
    "java": 1,"python": 2,"cpp" : 3,
    "backend" : 1,"frontend": 2,
    "junior" : 1,"senior":2,
    "chicken" : 2,"pizza" : 1
}

answer = []
db = {}

for i in info:                   # info에 대해 반복
    temp = i.split()
    conditions = temp[:-1]       # 조건들만 모으고, 점수 따로
    score = int(temp[-1])


    for n in range(5):           # 조건들에 대해 조합을 이용해서
        combi = list(combinations(range(4), n))
        print(combi)
        for c in combi:

            t_c = conditions.copy()
            # print(c,t_c)
            for v in c:          # '-'를 포함한 새로운 조건을 만들어냄.
                # print(t_c, "before",v)
                t_c[v] = '-'
                # print(t_c, "after")
            changed_t_c = '/'.join(t_c)
            if changed_t_c in db:     # 모든 조건의 경우에 수에 대해 딕셔너리
                db[changed_t_c].append(score)
            else:
                db[changed_t_c] = [score]

for value in db.values():             # 딕셔너리 내 모든 값 정렬
        value.sort()




