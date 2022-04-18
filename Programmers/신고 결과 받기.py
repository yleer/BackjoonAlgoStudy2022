import collections
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

k = 2
reportedDic = collections.defaultdict(int)
ireportyou = collections.defaultdict(list)

for i in range(len(report)):
    a = report[i].split(" ")

    if a[1] not in ireportyou[a[0]]:
        reportedDic[a[1]] += 1
        ireportyou[a[0]].append(a[1])



bannedArray = []



for key, value in reportedDic.items():
    # print(key,value)
    if value >= k:
        bannedArray.append(key)

answer = []

for id in id_list:
    cur = ireportyou[id]
    t = 0
    for b in cur:
        if b in bannedArray:
            t+=1

    answer.append(t)

print(answer)



