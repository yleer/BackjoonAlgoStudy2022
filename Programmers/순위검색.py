import re

info = ["java backend junior pizza 150","python frontend senior chicken 210",
        "python frontend senior chicken 150","cpp backend senior pizza 260",
        "java backend junior chicken 80","python backend senior chicken 50"
        ]


query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"
         ]


answer = []

for qu in query:
    # q = qu.split("and", " ")
    q = re.split('and |[ ]', qu)
    new = []
    # print(q)
    for i in range(len(q)):
        if q[i] != "":
            new.append(q[i])

    ans = 0
    for inf in info:
        data = inf.split(" ")

        if new[0] == "-" or new[0] == data[0]:
            if new[1] == "-" or new[1] == data[1]:
                if new[2] == "-" or new[2] == data[2]:
                    if new[3] == "-" or new[3] == data[3]:
                        if int(new[4]) <= int(data[4]):
                            ans += 1
                        else:
                            continue
                    else:
                        continue
                else:
                    continue

            else:
                continue
        else:
            continue


    answer.append(ans)


print(answer)